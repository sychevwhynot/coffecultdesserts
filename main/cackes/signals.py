from django.db.models.signals import post_delete
from django.dispatch import receiver

from cackes.models import CategoryImage


@receiver(post_delete, sender=CategoryImage)
def delete_image_file(sender, instance, **kwargs):
    """Удаляет файл с диска при удалении объекта CategoryImage."""

    if instance.image:
        instance.image.delete(save=False)
