from django.contrib import admin
from .models import Categoria,Producto,Cuenta_cliente,Boleta,Subcripcion
# Register your models here.

#permiso de administrar los modelos




admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Subcripcion)
admin.site.register(Cuenta_cliente)
admin.site.register(Boleta)
