# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barrios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre del Barrio')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radicado', models.CharField(max_length=30, verbose_name='Radicado')),
                ('fecha_solicitud', models.DateField()),
                ('proyecto', models.CharField(max_length=500, verbose_name='Nombre del Proyecto')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Propietarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('identificacion', models.CharField(max_length=20, verbose_name='Cedula')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licencias.Barrios')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_licencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Tipo de Licencia')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_usos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Tipo uso del suelo')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Area')),
                ('expediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licencias.Expediente')),
                ('tipo_uso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licencias.Tipo_usos')),
            ],
        ),
        migrations.AddField(
            model_name='expediente',
            name='propietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='licencias.Propietarios'),
        ),
        migrations.AddField(
            model_name='expediente',
            name='tipo_licencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licencias.Tipo_licencia'),
        ),
    ]