from django.contrib import admin
from .models import Page # Nombre de la clase


# Configuracion extra  para filtrar
class PageAdmin(admin.ModelAdmin):
    # Ver los campos de solo lectura
    readonly_fields = ('created_at','updated_at')
    # Incluir panel de busqueda para ciertos campos
    search_fields = ('title','content')
    # Poner lista de filtros segun el campo
    list_filter = ('visible',)
    # Que info se puede ver en el panel, por default solo esta el titulo
    list_display = ('title','visible','created_at')
    
# Register your models here.
admin.site.register(Page, PageAdmin)

# Configuracion del panel
title = 'Proyecton con Django'
subtitle = 'Panel de gestion'

# Aplicamos la conf.
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle