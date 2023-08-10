from typing import Any
from django.contrib import admin
from .models import Category, Article

# Clases para mostrar los campos de solo lectura
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']
    # Incluir panel de busqueda para ciertos campos
    search_fields = ('name','description')
    # Que info se puede ver en el panel, por default solo esta el titulo
    list_display = ('name','created_at')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at','update_at')
    # Incluir panel de busqueda para ciertos campos
    search_fields = ('title','content','user__username','category__name')
    # Poner lista de filtros segun el campo
    list_filter = ('public','user','categories')
    # Que info se puede ver en el panel, por default solo esta el titulo
    list_display = ('title','user','public','created_at')
    # Como el usuario es el iniciado, al guardar habra error, porque no estaremos
    # pasando ese campo. Aqui hacemos que detecte el usuario del loggin
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        # Identifico si no llego el id del usuario
        if not obj.user_id:
            # Defino el usario id ya que no esta
            obj.user_id = request.user.id 
        # Guardo el objeto
        obj.save()
    
# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)