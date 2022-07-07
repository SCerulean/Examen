from django.urls import path
from .views import form_mod_producto, home, inicio_sesion , form_Producto
#--from rest_framework import routers


urlpatterns = [
    path('', home, name="home"),
    path('inicio-sesion', inicio_sesion,name="inicio_sesion"),
    path('form-Producto', form_Producto, name="form_Producto"),
    path('form-mod-vehiculo/<id>', form_mod_producto, name="form_mod_producto")
]
