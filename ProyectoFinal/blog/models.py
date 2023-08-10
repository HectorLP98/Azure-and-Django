from django.db import models
from ckeditor.fields import RichTextField
# Modelo de usuarios que trae Django por default
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    
    # Campos del modelo
    
    name        = models.CharField(max_length=100,verbose_name='Nombre')
    description = models.CharField(max_length=250, verbose_name='Descripcion') 
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    
    # Configuracion para el panel de admin
    class Meta:
        # Nombre singular de la tabla
        verbose_name = 'Categoria'
        # Nombre plural
        verbose_name_plural = 'Categorias'
    
    # Configuracion para visualisacion de objetos
    def __str__(self):
        return self.name
    
class Article(models.Model):
    title      = models.CharField(max_length=150, verbose_name='titulo')
    content    = RichTextField(verbose_name='contenido')
    image      = models.ImageField(default='null',verbose_name='imagen',upload_to='articles')
    public     = models.BooleanField(verbose_name='¿Publicado?')
    # Generamos la relacion con el modelo User, usando la llave foranea
    user       = models.ForeignKey(User, verbose_name='usuario',editable=False, on_delete=models.CASCADE)
    # Generamos la relacion con el modelo categorias, estableciendo muchos articulos tienen muchas categorias, alternativamente puede buscar manytoone
    categories = models.ManyToManyField(Category, verbose_name='Categorias', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    update_at = models.DateTimeField(auto_now=True, verbose_name='actualizado')
    # Configuracion para el panel de admin
    class Meta:
        # Nombre singular de la tabla
        verbose_name = 'Articulo'
        # Nombre plural
        verbose_name_plural = 'Articulos'
    
    # Configuracion para visualisacion de objetos
    def __str__(self):
        return self.title