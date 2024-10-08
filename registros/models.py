from django.db import models
from django.utils import timezone
from sucursales.models import Sucursal
from personal.models import Personal
from gastos.models import Gasto


from productos.models import Producto




class RegistroVentas(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=0)
    inventario_inicial = models.PositiveIntegerField(default=0, null=True, blank=True)
    llegada_mercancia = models.PositiveIntegerField(default=0, null=True, blank=True)
    mercancia_defectuosa = models.PositiveIntegerField(default=0, null=True, blank=True)
    mercancia_sobrante = models.PositiveIntegerField(default=0, null=True, blank=True)
    fecha = models.DateField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, default= 0)  # Relación con Sucursal
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE, null=True, default= 0)

    def calcular_piezas_vendidas(self):
        # Fórmula para calcular piezas vendidas
        return (self.inventario_inicial + self.llegada_mercancia) - (self.mercancia_defectuosa + self.mercancia_sobrante)

    def calcular_total_ventas(self):
        # Fórmula para calcular el total en dinero
        return self.calcular_piezas_vendidas() * self.producto.precio


    def __str__(self):
        return f"{self.producto.nombre} - {self.fecha}"



















'''
class RegistroVentas(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    cambio = models.IntegerField(default=0, blank=True)
    dorado_inicial = models.IntegerField(default=0,blank=True)
    dorado_llego = models.IntegerField(default=0, blank=True)
    dorado_roto = models.IntegerField(default=0, blank=True)
    dorado_sobro = models.IntegerField(default=0, blank=True)
    oreo_inicial = models.IntegerField(default=0, blank=True)
    oreo_llego = models.IntegerField(default=0, blank=True)
    oreo_roto = models.IntegerField(default=0, blank=True)
    oreo_sobro = models.IntegerField(default=0, blank=True)
    doble_inicial = models.IntegerField(default=0, blank=True)
    doble_llego = models.IntegerField(default=0, blank=True)
    doble_roto = models.IntegerField(default=0, blank=True)
    doble_sobro = models.IntegerField(default=0, blank=True)
    sundae_inicial = models.IntegerField(default=0, blank=True)
    sundae_llego = models.IntegerField(default=0, blank=True)
    sundae_roto = models.IntegerField(default=0, blank=True)
    sundae_sobro = models.IntegerField(default=0, blank=True)
    vainilla_inicial = models.IntegerField(default=0, blank=True)
    vainilla_llego = models.IntegerField(default=0, blank=True)
    vainilla_roto = models.IntegerField(default=0, blank=True)
    vainilla_sobro = models.IntegerField(default=0, blank=True)
    chocolate_inicial = models.IntegerField(default=0, blank=True)
    chocolate_llego = models.IntegerField(default=0, blank=True)
    chocolate_roto = models.IntegerField(default=0, blank=True)
    chocolate_sobro = models.IntegerField(default=0, blank=True)
    gastos=models.IntegerField(default=0, blank=True)
    a_cuenta= models.IntegerField(default=0, blank=True) 
    entrego=models.IntegerField(default=0, blank=True)

  '''
