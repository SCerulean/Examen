from ast import Return
from email import message
from urllib import request
from django.shortcuts import render,redirect
from .forms  import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .models import Cuenta_cliente, Producto
from .forms import ProductoForm




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



def catalogo_perfil(request):
    return render(request,'core/inicio_Catalogo_perfil.html')


def Registrar_cuenta(request):
    if request.method == 'POST':    
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'usuario {username} creado')
    else :
        form = UserCreationForm()

    context = {'form' : form}

    return render(request,'core/Registrarce.html',context)


def Registrar_cuenta2(request):
    return render(request,'core/Registrarce.html')



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


#################################################################################

def button_login(request):
    return render(request,"core/inicio_sesion.html")

def button_logout(request):
    return redirect(to="home")