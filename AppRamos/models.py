from django.db import models

from django.db import models

class Datos(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()


# Create your models here.
