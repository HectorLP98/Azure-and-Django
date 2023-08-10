from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
    #nombre a mostrar en el panel de admin
    verbose_name = 'Gestion del Blog'
