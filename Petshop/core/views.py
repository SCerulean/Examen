from django.shortcuts import render
from .models import Productos

# Create your views here.
def home (request):
    return render(request,' core/inicio_Catalogo.html ')

def create_acount(request):
    return render(request,' core/create_acount_form.html ')

def inicio_sesion(request):
    return render(request,' core/inicio_sesion.html ')

def form_Producto(request):
    return render(request, ' core/form_Producto.html ')

########################################################################

#Traer Productos de la tabla

def Producto(request):
    Producto = Productos.objects.all()

#Pasar los datos de los productos la template

datos = {
    ' Productos ' : Producto
}

# Se envia al template 

#return render(request, ' core/inicio_Catalogo.html ',datos)

#########################################################################

