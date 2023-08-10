from django.shortcuts import render
from .models import Page
# Decorador para pedir estar logeado, da seguridad y privacidad a las paginas.
from django.contrib.auth.decorators import login_required


# Instancio el decorador y en caso de no estar logeado me llevara al url cuyo name=login
@login_required(login_url='login')
# Create your views here.
def page(request, slug):
    
    # Extraigo los datos cuando slug=slug
    page = Page.objects.get(slug=slug)
    # Creo datos de salida
    datos = {
        'page' : page
    }
    return render(request,'page.html', datos)