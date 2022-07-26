from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)


class TipoInmueble(models.Model):
    tipo_inmueble = models.TextField()


class Comuna(models.Model):
    comuna = models.TextField()


class Region(models.Model):
    region = models.TextField()


class TipoUser(models.Model):
    tipo_user = models.TextField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_tipo_user = models.ForeignKey('m7_python.TipoUser', on_delete=models.CASCADE, null=True)
    rut = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=12)
    correo = models.CharField(max_length=50)


class Inmuebles(models.Model):
    id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    id_tipo_inmueble = models.ForeignKey('m7_python.TipoInmueble', on_delete=models.CASCADE, null=True)
    id_comuna = models.ForeignKey('m7_python.Comuna', on_delete=models.CASCADE, null=True)
    id_region = models.ForeignKey('m7_python.Region', on_delete=models.CASCADE, null=True)
    nombre_inmueble = models.TextField()
    descripcion = models.CharField(max_length=200)
    m2_construido = models.FloatField()
    m2_terreno = models.FloatField()
    numero_estacionamientos = models.PositiveIntegerField(default=0)
    numero_banos = models.PositiveIntegerField(default=0)
    numero_hab = models.PositiveIntegerField(default=0)
    direccion = models.CharField(max_length=200)
    precio_mensual = models.PositiveIntegerField()
    estado = models.BooleanField(default=False)
