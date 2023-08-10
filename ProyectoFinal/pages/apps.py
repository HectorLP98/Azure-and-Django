from django.apps import AppConfig


class PagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pages"
    # Nombre mostrado en el panel de administracion
    verbose_name = 'Gestion de paginas'
