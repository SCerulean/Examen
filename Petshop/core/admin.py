from django.contrib import admin

# Register your models here.

from .models import Categorías, Productos

#permiso de administrar los modelos

admin.site.register(Categorías)
admin.site.register(Productos)
