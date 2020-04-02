from django.db import models


# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    domicilio = models.TextField(max_length=70)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)

    def full_name(self):
        return self.nombre + ' ' + self.apellidos


class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()
