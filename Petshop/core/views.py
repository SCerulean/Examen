from ast import Return
from urllib import request
from django.shortcuts import render,redirect
from .forms import registro




# Create your views here.

def home (request):
    return render(request,'core/inicio_Catalogo.html')

def create_acount(request):
    return render(request,'core/create_acount_form.html')

def inicio_sesion(request):

    
    return render(request,'core/inicio_sesion.html')

def Registrar_cuenta(request):
    datos = {'form': registro()}
    if request.method == 'POST':
        formulario = registro(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"

    return render(request,'core/Registrarce.html',datos)

def form_Producto(request):
    return render(request, 'core/Form_Producto.html')

#################################################################################

# Post
def form_Producto(request): 
    datos = {
        'form': ProductoForms()
    }

    if request.method == 'POST':
        formulario = ProductoForms(data=request.POST, instance=Productos)
        if formulario.is_valid:
            formulario.save()

            datos['mensaje'] = "Guardados Correctamente"

    return render (request, 'core/Form_Producto.html',datos)

#################################################################################

#modificar
def form_mod_producto(request,id):
    producto = Productos.objects.get(IDProducto=id)
    datos = {
        'form': ProductoForms(instance=Productos)
    }
    return render(request,'core/Form_Mod_Producto.html',datos)

#################################################################################

def form_del_producto(request, id):
    Productos = Productos.objects.get(IDProducto=id)
    Productos.delete()
    return redirect(to="ListadoProductos")

#################################################################################

#Traer datos
def TraerDatos(request):
    Producto = Productos.objects.all()

    datos = {
        'Productos' : Producto
    }

    return render(request, 'inicio_Catalogo.html',datos)

#################################################################################