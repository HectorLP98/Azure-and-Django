from django.shortcuts import render, get_object_or_404, redirect
# Objeto para formulario de usuarios
#from django.contrib.auth.forms import UserCreationForm
from MainApp.forms import RegisterForm
#Para mensaje flash
from django.contrib import messages
# Para login
from django.contrib.auth import authenticate, login, logout
# Decorador para pedir estar logeado, da seguridad y privacidad a las paginas.
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    '''
    (Function)
        Pagina de inicio
    '''
    # Lo dirigo al html que esta en templates
    return render(request,'mainapp/index.html', {'title':'Mi Portafolio'})

def register_page(request):
    
    # Revisamos si hay un usuario autenticado
    if request.user.is_authenticated:
        return redirect('index')
    # En caso de no estar se mostrara el formulario
    else:
        # Generamos el formulario de login
        register_form = RegisterForm()
        
        # Revisamos que si nos llego un POST
        if request.method == 'POST':
            # Llenamos el form con la info que trae
            register_form = RegisterForm(request.POST)
            
            # Revisamos que sea valido
            if register_form.is_valid():
                # Guardamos al usuario
                register_form.save()
                
                # Como todo ha salido bien mandamos msj flask
                messages.success(request,'Registro exitoso!!')
                return redirect('index')
        
        datos = {'title':'Registro',
                'register_form':register_form}
        return render(request,'users/register.html',datos)

def login_page(request):
    
    # Revisamos que nos llego un POST
    if request.method == 'POST':
        # Extraigo los datos de la vairable username
        username = request.POST.get('username')
        # Extraigo los datos de la variable password
        password = request.POST.get('password')
        
        # Se realiza la autenticacion
        user = authenticate(request=request, username=username, password=password)
        
        # En caso de existir el usuario, la variable user sera distinta de None
        if user is not None:
            # Logeamos al usuario
            login(request=request, user=user)
            
            return redirect('index')
        else:
            # No existe el usuario
            messages.warning(request=request, message='Credenciales no validas, intentelo de nuevo!!. ')
            
            
    datos = {'title':'Login'}
    
    return render(request, 'users/login.html',datos)

# Instancio el decorador y en caso de no estar logeado me llevara al url cuyo name=login
@login_required(login_url='login')
def logout_page(request):
    # Cierro sesion
    logout(request=request)
    
    # Redirijo al login
    return redirect('login')