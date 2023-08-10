from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Clase con el modelo personalizado, hereda el UserCreationForm pero le agregamos mas cositas
class RegisterForm(UserCreationForm):
    class Meta:
        model = User 
        # Campos que queremos que se llenen, son del modelo de USer
        fields = ['username','email','first_name','last_name','password1','password2']