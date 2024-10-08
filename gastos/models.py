from django.db import models


# Create your models here.
class Gasto(models.Model):
    descripcion = models.TextField(verbose_name='Descripción')
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Monto')
    fecha = models.DateField(verbose_name='Fecha')
    registro_diario = models.ForeignKey('registros.RegistroVentas', on_delete=models.CASCADE, related_name='gastos_diarios')  # Relación con RegistroDiario


    def __str__(self):
        return f"{self.descripcion} - ${self.monto}"