from django.urls import path
from . import views


urlpatterns = [
    path('articles/',views.list_articles, name='list_articles'),
    path('aritcle/<int:id_article>', views.article,name='articulo')
]