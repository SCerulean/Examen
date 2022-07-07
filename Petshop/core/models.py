from tabnanny import verbose
from django.db import models

# Create your models here.

#modelo Categorías

class Categorías (models.Model):
    idCategoría = models.IntegerField(primary_key=True, verbose_name=' ID DE LA CATEGORIA ')
    NombreCategoría = models.CharField(max_length=50, verbose_name=' NOMBRE DE LA CATEGORIA ')

    def __str__(self):
        return self.NombreCategoría

#modelo Productos

class Productos (models.Model):
    IDProducto = models.IntegerField(primary_key=True, verbose_name= ' ID PRODUCTO ')
    NombreProducto = models.CharField(max_length=20, verbose_name=' NOMBRE PRODUCTO ')
    MarcaProducto = models.CharField(max_length=20, verbose_name=' MARCA ')
    PrecioProducto = models.IntegerField(verbose_name=' PRECIO ')

    def __str__(self):
        return self.NombreProducto

