from django.db.models import Prefetch
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from cackes.forms import OrderForm
from cackes.models import (
    CategoryCackes,
    CategoryImage,
    Order
)
from cackes.utils import send_admin_notification


class MainPageView(CreateView):
    """Главная страница с формой заказа."""

    model = Order
    form_class = OrderForm
    template_name = 'home_page.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        main_images = CategoryImage.objects.filter(is_main=True)
        context['categories'] = (
            CategoryCackes.objects
            .filter(is_active=True)
            .prefetch_related(Prefetch('images', queryset=main_images, to_attr='main_images'))
        )

        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        send_admin_notification(self.object)
        return response


class CategoryDetailView(DetailView):
    """Страница категории."""

    model = CategoryCackes
    template_name = 'category_page.html'
    context_object_name = 'category'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return CategoryCackes.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_images'] = (
            self.object.images
            .order_by('-is_main', '-created_at')
        )
        return context


@require_POST
def order_submit(request):
    """Обработка AJAX-отправки формы заказа."""

    form = OrderForm(request.POST)

    if form.is_valid():
        order = form.save()

        mail = send_admin_notification(order)

        if mail:
            return JsonResponse({
                'success': True,
                'message': 'Заявка отправлена! Скоро мы с вами свяжемся',
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Технические проблемы. Попробуйте позже.',
            })

    errors = form.errors.get_json_data()
    simple_errors = {
        field: [e['message'] for e in errs]
        for field, errs in errors.items()
    }
    return JsonResponse(
        {'success': False, 'errors': simple_errors},
        status=400,
    )
