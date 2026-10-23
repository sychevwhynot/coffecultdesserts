import logging

from django.conf import settings
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


def send_admin_notification(order):
    """Отправка уведомления администратору о новом заказе."""

    try:
        subject = f'Новый заказ #{order.id} от {order.name}'

        message = (
            f'Новый заказ #{order.id}\n'
            f'\n'
            f'ФИО: {order.name}\n'
            f'Почта: {order.email}\n'
            f'Телефон: {order.phone}\n'
            f'Комментарий: {order.comment}\n'
            f'Дата создания: {order.created_at:%d.%m.%Y %H:%M}\n'
            f'\n'
            f'Ссылка в админку: '
            f'https://cake71.ru/admin/orders/order/{order.id}/change/'
        )

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.MAILERS["default"]["OPTIONS"]["username"],
            recipient_list=[settings.MAILERS["default"]["OPTIONS"]["username"]],
            fail_silently=False,
        )

        return True
    except Exception:
        logger.exception("Не удалось отправить письмо по заказу #%s", order.id)
        return False