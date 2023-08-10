from django.db import models
# Libreria para texto enriquecido
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    
    # Columnas del modelo
    title   = models.CharField(max_length=75,verbose_name='Titulo')
    content = RichTextField(verbose_name='Contenido')
    order   = models.IntegerField(default=0, verbose_name='Orden')
    slug    = models.CharField(unique=True, max_length=200, verbose_name='URL_amigable')
    visible = models.BooleanField(verbose_name='Publicado?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    
    class Meta:
        # Nombre singular en el panel de admin
        verbose_name = 'Pagina'
        # Nombre plural en el panel de admin
        verbose_name_plural = 'Paginas'
        
    def __str__(self) -> str:
        return self.title