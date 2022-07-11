from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm, Widget
from .models import Cuenta_cliente

        
class registro (ModelForm):
         
    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={"placeholder": "Escribe tu nombre"}))
    correo = forms.CharField(label="Correo",widget=forms.TextInput(attrs={"placeholder": "Escribe tu email"}))
    contraseña = forms.CharField(label="Contraseña",widget=forms.TextInput(attrs={"placeholder": "Escribe tu contraseña"}))
    contraseña2 = forms.CharField(label="Repita su Contraseña",widget=forms.TextInput(attrs={"placeholder": ""}))
    class Meta :
        model = Cuenta_cliente
        fields= ['nombre','correo','contraseña','contraseña2',]


class login (ModelForm):
         
    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={"placeholder": "Escribe tu nombre"}))
    contraseña = forms.CharField(label="Contraseña",widget=forms.TextInput(attrs={"placeholder": "Escribe tu contraseña"}))
    class Meta :
        model = Cuenta_cliente
        fields= ['nombre','contraseña',]
   
