from django.db import models

# Create your models here.
class Sucursal(models.Model):
    nombre_sucursal = models.CharField(max_length=255)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre_sucursal