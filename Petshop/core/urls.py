from django.urls import path
from .views import  modificar_producto, home, inicio_sesion , agregar_Producto, Registrar_cuenta,ListadoProductos,delete_Producto

#--from rest_framework import routers


urlpatterns = [
    path('', home, name="home"),
    path('inicio-sesion', inicio_sesion,name="inicio_sesion"),
    path('Crear-cuenta',Registrar_cuenta ,name="Registrar_cuenta"),
    path('agregar-Producto', agregar_Producto, name="agregar_Producto"),
    path('lista-productos/<id>',delete_Producto, name="delete_Producto"),
    path('modificar-producto/<id>', modificar_producto, name="modificar_producto"),
    path('lista-productos',ListadoProductos, name="lista_productos"),
]
