from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CategoryCackes(models.Model):
    """Модель категорий десертов."""

    name = models.CharField(
        max_length=100,
        verbose_name='Название категории',
        unique=True,
        db_index=True 
    )
    description = models.TextField(
        verbose_name='Описание категории',
        blank=True,
        null=True
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='URL',
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активна'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class CategoryImage(models.Model):
    """Фотография, привязанная к категории."""

    category = models.ForeignKey(
        CategoryCackes,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Категория',
    )
    image = models.ImageField(
        upload_to='categories/',
        verbose_name='Фото',
    )
    is_main = models.BooleanField(
        default=False,
        verbose_name='Главное фото',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Загружено',
    )

    class Meta:
        verbose_name = 'Фото категории'
        verbose_name_plural = 'Фото категорий'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.category.name} — {self.image.name}'


class Order(models.Model):
    """Модель для заказов."""

    name = models.CharField(
        max_length=100,
        verbose_name='ФИО',
    )
    email = models.EmailField(
        max_length=100,
        verbose_name='Почта'
    )
    phone = PhoneNumberField(
        verbose_name='Номер телефона',
        max_length=20,
        region='RU'
    )
    comment = models.TextField(
        max_length=1000,
        verbose_name='Комментарий'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    send_mail = models.BooleanField(
        default=False,
        verbose_name='Письмо отправлено?'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
