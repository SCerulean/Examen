from django.urls import path
from .views import home, inicio_sesion , form_Producto
#--from rest_framework import routers


urlpatterns = [
    path('', home, name="home"),
    path('inicio-sesion', inicio_sesion,name="inicio_sesion"),
    path('form_Producto', form_Producto, name="form_Producto")
]
