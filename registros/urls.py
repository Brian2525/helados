from django.urls import include, path
from . import views



urlpatterns = [
    path('registros/', views.crear_registro_diario_todos_productos, name='registrar'),
    path('resultados/', views.resultado_todos_productos, name='resultado'),
    path('resultadoshoy/', views.calcular_venta_hoy, name='resultadohoy')
]