from django.urls import path
from django.views.generic import TemplateView

from cackes.views import (
    CategoryDetailView,
    MainPageView,
    order_submit
)


urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('order/', order_submit, name='order_submit'),
    path('policy/', TemplateView.as_view(template_name='policy.html'), name='policy'),
    path('personal/', TemplateView.as_view(template_name='personal.html'), name='personal'),
]
