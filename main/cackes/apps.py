from django.apps import AppConfig


class CackesConfig(AppConfig):
    name = 'cackes'
    verbose_name = 'Десерты'

    def ready(self):
        from cackes import signals
