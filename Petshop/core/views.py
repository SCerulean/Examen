from ast import Return
from urllib import request
from django.shortcuts import render

from core.forms import ProductoForms
from .models import Productos

# Create your views here.

def home (request):
    return render(request,'core/inicio_Catalogo.html')

def create_acount(request):
    return render(request,'core/create_acount_form.html')

def inicio_sesion(request):
    return render(request,'core/inicio_sesion.html')

def form_Producto(request):
    return render(request, 'core/Form_Producto.html')

# Post
def form_Producto(request): 
    datos = {
        'form': ProductoForms()
    }

    if request.method == 'POST':
        formulario = ProductoForms(request.POST)
        if formulario.is_valid:
            formulario.save()

            datos['mensaje'] = "Guardados Correctamente"

    return render (request, 'core/Form_Producto.html',datos)

def TraerDatos(request):
    Producto = Productos.objects.all()

    datos = {
        'Productos' : Producto
    }

    return render(request, 'inicio_Catalogo.html',datos)

