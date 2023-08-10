from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category
#objeto para paginar
from django.core.paginator import Paginator
# Decorador para pedir estar logeado, da seguridad y privacidad a las paginas.
from django.contrib.auth.decorators import login_required

# Instancio el decorador y en caso de no estar logeado me llevara al url cuyo name=login
@login_required(login_url='login')
# Create your views here.
def list_articles(request):
    # Extraemos los articulos
    articles = Article.objects.all()
    
    # Paginar los articulos
    paginator = Paginator(articles,per_page=1)
    
    # Recoger numero de pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    
    # Diccionario de datos a retornar
    datos = {
        'title':'Lista de articulos',
        'articles': page_articles
    }
    return render(request,'articles/list_articles.html',datos)

# Instancio el decorador y en caso de no estar logeado me llevara al url cuyo name=login
@login_required(login_url='login')
def article(request,id_article):
    # Jalamos los articulos segun el id, y en caso de no existir nos regresa un error 404
    article = get_object_or_404(Article,id=id_article)
    
    datos = {'article':article}
    return render(request,'articles/articles_details.html',datos)
    
    