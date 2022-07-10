from tabnanny import verbose
from tkinter import CASCADE
from django.db import models

# Create your models here.

#modelo Categorías


class Categoria (models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name=' ID DE LA CATEGORIA ')
    NombreCategoría = models.CharField(max_length=50, verbose_name=' NOMBRE DE LA CATEGORIA ')

    def __str__(self):
        return self.NombreCategoría

#modelo Productos

class Producto(models.Model):
    SKU = models.CharField(max_length=6 ,primary_key=True ,verbose_name='SKU')      
    nombre =  models.CharField(max_length=50 ,verbose_name='nombre')      
    precio = models.IntegerField(verbose_name='precio')
    stock = models.IntegerField(verbose_name='stock')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre 



class Subcripcion(models.Model):
    estado = models.CharField(max_length=2, primary_key= True ,verbose_name='estado' )
    def __str__(self) -> str:
        return self.estado   


class Cuenta_cliente(models.Model):
    nombre = models.CharField(max_length=20 ,primary_key=True ,verbose_name='nombre') 
    correo = models.CharField(max_length=100,verbose_name='correo')
    contraseña = models.CharField(max_length=50,verbose_name='contrasena')
    sub_usu = models.ForeignKey(Subcripcion,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre  



class Boleta(models.Model):
    id_boleta = models.IntegerField(primary_key=True ,verbose_name='id boleta')   
    nombre_usu = models.ForeignKey(Cuenta_cliente,on_delete=models.CASCADE)          
    producto_SKU = models.ForeignKey(Producto,on_delete=models.CASCADE) 
    cantidad = models.IntegerField(verbose_name='cantidad')
    total = models.IntegerField(verbose_name='total')
    
    def __str__(self) -> str:
        return self.nombre 
