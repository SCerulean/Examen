# Generated by Django 3.2.13 on 2022-07-10 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_auto_20220710_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name=' ID DE LA CATEGORIA ')),
                ('NombreCategoría', models.CharField(max_length=50, verbose_name=' NOMBRE DE LA CATEGORIA ')),
            ],
        ),
        migrations.CreateModel(
            name='Subcripcion',
            fields=[
                ('estado', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='estado')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('SKU', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='SKU')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('precio', models.IntegerField(verbose_name='precio')),
                ('stock', models.IntegerField(verbose_name='stock')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta_cliente',
            fields=[
                ('nombre', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='nombre')),
                ('contraseña', models.CharField(max_length=50, verbose_name='contrasena')),
                ('correo', models.CharField(max_length=100, verbose_name='correo')),
                ('sub_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subcripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.IntegerField(primary_key=True, serialize=False, verbose_name='id boleta')),
                ('cantidad', models.IntegerField(verbose_name='cantidad')),
                ('total', models.IntegerField(verbose_name='total')),
                ('nombre_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cuenta_cliente')),
                ('producto_SKU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
    ]
