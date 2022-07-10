from django.urls import path
from .views import form_del_producto, form_mod_producto, home, inicio_sesion , form_Producto, Registrar_cuenta
#--from rest_framework import routers


urlpatterns = [
    path('', home, name="home"),
    path('inicio-sesion', inicio_sesion,name="inicio_sesion"),
    path('Crear-cuenta',Registrar_cuenta ,name="Registrar_cuenta"),
    path('form-Producto', form_Producto, name="form_Producto"),
    path('form-mod-vehiculo/<id>', form_mod_producto, name="form_mod_producto"),
    path('form-del-vehiculo/<id>', form_del_producto, name="form_del_producto")
]
