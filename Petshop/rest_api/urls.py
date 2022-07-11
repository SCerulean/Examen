from django.urls import path
from rest_api.views import detalle_producto, lista_Producto
from .viewslogin import login


urlpatterns = [
    
    path ('lista_Productos',lista_Producto,name='lista_Producto'),
    path('detalle_producto/<id>',detalle_producto,name='detalle_producto'),
    path('login',login,name='login'),
]
