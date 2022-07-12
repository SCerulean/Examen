from django.urls import path
from .views import  modificar_producto,Registrar_cuenta2, home,catalogo_perfil , agregar_Producto, Registrar_cuenta,ListadoProductos,delete_Producto,button_login,button_logout
from django.contrib.auth.views import LoginView, LogoutView
#--from rest_framework import routers


urlpatterns = [
    path('', home, name="home"),
    path('catalogo-perfil', catalogo_perfil, name="catalogo_perfil"),
    path('login/', LoginView.as_view(template_name = 'core/inicio_sesion.html'),name="login"),
    path('', LogoutView.as_view(template_name = 'core/inicio_Catalogo'),name="home"),
    path('Crear-cuenta',Registrar_cuenta ,name="Registrar_cuenta"),
    path('Crear-cuenta',Registrar_cuenta2 ,name="Registrar_cuenta2"),
    path('agregar-Producto', agregar_Producto, name="agregar_Producto"),
    path('lista-productos/<id>',delete_Producto, name="delete_Producto"),
    path('login/',button_login, name="button_login"),
    path('logout/',button_logout, name="button_logout"),
    path('modificar-producto/<id>', modificar_producto, name="modificar_producto"),
    path('lista-productos',ListadoProductos, name="lista_productos"),
]
