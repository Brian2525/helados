from django.contrib import admin
from .models import Gasto
# Register your models here.


class gastoAdmin(admin.ModelAdmin): 
    list_display=('descripcion', 'monto', 'fecha')

admin.site.register(Gasto)