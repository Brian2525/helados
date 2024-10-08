from django.contrib import admin
from .models import RegistroVentas


class registroVentasAdmin(admin.ModelAdmin): 
    list_display=('personal', 'sucursal', 'fecha')

admin.site.register(RegistroVentas)