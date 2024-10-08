from django.db import models

# Create your models here.
class Personal(models.Model):
    TURNOS = [
        ('S-D', 'Sab-dom'),
        ('L-V', 'Lun-viernes'),
    ]

    nombre = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    datos_transferencia = models.TextField()
    turno = models.CharField(max_length=5, choices=TURNOS)

    def __str__(self):
        return self.nombre