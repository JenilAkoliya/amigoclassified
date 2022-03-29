from django.apps import AppConfig


class HopifyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hopify'

    def ready(self):
        import hopify.signals
