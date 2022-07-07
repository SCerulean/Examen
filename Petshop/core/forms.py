from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Productos

# Clase ProductosForm --

class ProductoForms(ModelForm):

    class Meta:
        model = Productos
        fields = ['IDProducto','NombreProducto','MarcaProducto','PrecioProducto']
