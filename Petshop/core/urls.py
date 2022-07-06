from django.urls import path
from .views import home, inicio_sesion
#--from rest_framework import routers



urlpatterns = [
    path('', home, name="home"),
    path("inicio-sesion",inicio_sesion,name="inicio_sesion")
]