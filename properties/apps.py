# properties/apps.py
from django.apps import AppConfig


class PropertiesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "properties"

    def ready(self):
        # Import signal handlers so they register on app load
        from . import signals  # noqa: F401
