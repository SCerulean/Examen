from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Widget
from .models import Cuenta_cliente,Producto

        
class UserCreationForm (UserCreationForm):
    username = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={"placeholder": "Escribe tu nombre"}))
    email = forms.CharField(label="Correo",widget=forms.EmailInput)
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita su contraseña",widget=forms.PasswordInput)
   
    class Meta :
        model = User
        fields= ['username','email','password1','password2',]
        help_texts = {k:"" for k in fields}


class login (ModelForm):
         
    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={"placeholder": "Escribe tu nombre"}))
    contraseña = forms.CharField(label="Contraseña",widget=forms.TextInput(attrs={"placeholder": "Escribe tu contraseña"}))
    class Meta :
        model = Cuenta_cliente
        fields= ['nombre','contraseña',]


class ProductoForm (ModelForm):
    class Meta :
        model = Producto
        fields= ['SKU','nombre','precio','stock','categoria',]

   
