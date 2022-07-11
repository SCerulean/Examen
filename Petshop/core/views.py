from ast import Return
from urllib import request
from django.shortcuts import render,redirect

from .models import Producto
from .forms import registro,ProductoForm




# Create your views here.

def home (request):
    return render(request,'core/inicio_Catalogo.html')




def delete_Producto(request, id):
    producto = Producto.objects.get(SKU=id)
    producto.delete()
    return redirect(to="lista_productos")

def ListadoProductos (request):

    producto  = Producto.objects.all()
    datos = {'producto': producto}
    return render(request,'core/ListadoProductos.html',datos)




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


#################################################################################

# Post
def agregar_Producto(request): 
    datos = {'form': ProductoForm()}
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
            
    return render(request, 'core/form_Producto.html', datos)

#################################################################################

#modificar
def modificar_producto(request,id):
    producto = Producto.objects.get(SKU=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/Form_Mod_Producto.html', datos)

#################################################################################

#Traer datos
def TraerDatos(request):
    Producto = Producto.objects.all()

    datos = {
        'Productos' : Producto
    }

    return render(request, 'inicio_Catalogo.html',datos)

#################################################################################