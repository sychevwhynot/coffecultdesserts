from django.contrib import admin
from django.utils.html import format_html

from cackes.models import (
    CategoryCackes,
    CategoryImage,
    Order
)


class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    extra = 1
    fields = ('preview', 'image', 'is_main')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if not obj.image:
            return ''
        return format_html(
            '<a href="{0}" target="_blank">'
            '<img src="{0}" style="max-height: 80px; border-radius: 6px;" />'
            '</a>',
            obj.image.url,
        )
    preview.short_description = 'Превью'


@admin.register(CategoryCackes)
class CategoryCackesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CategoryImageInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'send_mail', 'created_at']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['created_at', 'send_mail']
    ordering = ['-created_at']
