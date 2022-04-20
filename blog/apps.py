from django.apps import AppConfig
from django.db.models.signals import post_save


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        from .signals import edit_signal
        post_save.connect(edit_signal, sender=self)
