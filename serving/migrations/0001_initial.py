# Generated by Django 5.0.4 on 2024-04-08 22:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(null=True)),
                ('ubicacion', models.TextField(null=True)),
                ('telefono', models.CharField(max_length=200, verbose_name='telefono')),
                ('correo', models.EmailField(max_length=254)),
                ('tipo', models.CharField(max_length=200, verbose_name='Tipo')),
                ('nombreUnidad', models.CharField(max_length=200, verbose_name='Nombre de la Unidad')),
                ('comandante', models.CharField(max_length=200, verbose_name='Comandante')),
            ],
        ),
        migrations.CreateModel(
            name='ArticuloModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoEquipo', models.CharField(max_length=100, verbose_name='Codigo de Equipo')),
                ('descripcionGeneral', models.TextField()),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('serial', models.CharField(max_length=200)),
                ('fechaIngreso', models.DateField(auto_now_add=True)),
                ('estadoActual', models.BooleanField(default=False)),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serving.unidadmodel')),
            ],
        ),
    ]
