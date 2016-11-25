from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


# Autor: Pedro.
# Descripcion: Modelo  para parametrizar  los tipos de licencias de construccion
# Fecha: 18 Nov 2016
@python_2_unicode_compatible
class Tipo_licencia(models.Model):
    nombre = models.CharField("Tipo de Licencia", max_length=100, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

# Autor: Pedro.
# Descripcion: Modelo  para parametrizar  los barrios del municipio de arauca, es una tabla geografica (pendiente de implementar)
# Fecha: 18 Nov 2016
@python_2_unicode_compatible
class Barrios(models.Model):
    nombre = models.CharField("Nombre del Barrio", max_length=100, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


# Autor: Pedro.
# Descripcion: Modelo para la administracion de los propietarios (se asume que el proceso contempla el registro de un unico proppietario
# Fecha: 18 Nov 2016
@python_2_unicode_compatible
class Propietarios(models.Model):
    nombres = models.CharField("Nombres", max_length=100)
    apellidos = models.CharField("Apellidos", max_length=100)
    identificacion = models.CharField("Cedula", max_length=20)
    direccion = models.CharField("Direccion", max_length=100)
    barrio = models.ForeignKey(Barrios)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombres



# Autor: Pedro.
# Descripcion: Modelo para la  administracion de los expedientes de las licencias urbanisticas
# Fecha: 18 Nov 2016
@python_2_unicode_compatible
class Expediente(models.Model):
    radicado = models.CharField("Radicado", max_length=30)
    fecha_solicitud = models.DateField()
    tipo_licencia = models.ForeignKey(Tipo_licencia)
    proyecto = models.CharField("Nombre del Proyecto", max_length=500)
    propietario = models.ForeignKey(Propietarios, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.proyecto


# Autor: Pedro.
# Descripcion: Modelo para parametrizar los tipos de uso del suelo
# Fecha: 18 Nov 2016
@python_2_unicode_compatible
class Tipo_usos(models.Model):
    nombre = models.CharField("Tipo uso del suelo", max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


# Autor: Pedro.
# Descripcion: Modelo que administra los usos de suelo por cada expediente
# Fecha: 18 Nov 2016
@python_2_unicode_compatible
class Usos(models.Model):
    expediente = models.ForeignKey(Expediente)
    tipo_uso = models.ForeignKey(Tipo_usos)
    area = models.DecimalField("Area", max_digits=9, decimal_places=6)

    def __str__(self):
        return self.expediente


# Autor: Pedro.
# Descripcion: Modelo que administra los usos de suelo por cada expediente
# Fecha: 18 Nov 2016
@python_2_unicode_compatible
class icnonos(models.Model):
    nombre = models.CharField(max_length=10)
    upload = models.FileField(upload_to='licencias/img/')

    def __str__(self):
        return self.nombre
