from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .models import  RegistroVentas
from productos.models import Producto
from gastos.models import Gasto
from .forms import RegistroDiarioTodosProductosForm
from django.shortcuts import render
from django.utils import timezone




def crear_registro_diario_todos_productos(request):
    if request.method == 'POST':
        form = RegistroDiarioTodosProductosForm(request.POST)
        if form.is_valid():
            sucursal_seleccionada = form.cleaned_data['sucursal']  # Capturamos la sucursal seleccionada
            personal_seleccionado = form.cleaned_data['personal'] 
            fecha_registro = form.cleaned_data['fecha']
            productos = Producto.objects.all()
            
            
            
            
            for producto in productos:
                inventario_inicial = form.cleaned_data[f'inventario_inicial_{producto.id}']
                llegada_mercancia = form.cleaned_data[f'llegada_mercancia_{producto.id}']
                mercancia_defectuosa = form.cleaned_data[f'mercancia_defectuosa_{producto.id}']
                mercancia_sobrante = form.cleaned_data[f'mercancia_sobrante_{producto.id}']
                
                # Crear un registro diario para cada producto
                registro = RegistroVentas(
                    producto=producto,
                    inventario_inicial=inventario_inicial,
                    llegada_mercancia=llegada_mercancia,
                    mercancia_defectuosa=mercancia_defectuosa,
                    mercancia_sobrante=mercancia_sobrante,
                    fecha=fecha_registro,
                    sucursal=sucursal_seleccionada,  # Asignamos la sucursal seleccionada
                    personal=personal_seleccionado,
                    
                )
                print(registro)
                registro.save()
                  # Verificar si se ingresaron datos de gastos
            descripcion_gasto = form.cleaned_data.get('descripcion_gasto')
            monto_gasto = form.cleaned_data.get('monto_gasto')
                
            if descripcion_gasto and monto_gasto:
                    # Crear un nuevo gasto y asociarlo al registro diario
                gasto = Gasto(
                    descripcion=descripcion_gasto,
                    monto=monto_gasto,
                    fecha=fecha_registro,
                    registro_diario=registro
                )
                gasto.save()
                  # Guardar el registro

            return redirect('resultado')  # Redirigir a una página de éxito o resultado
    else:
        form = RegistroDiarioTodosProductosForm()

    return render(request, 'crear_registro_todos_productos.html', {'form': form})



def resultado_todos_productos(request):
    registros = RegistroVentas.objects.all().order_by('-fecha')  # Ordenar por la fecha más reciente
    return render(request, 'resultado_todos_productos.html', {'registros': registros}) 





def calcular_venta_hoy(request):
    registros = RegistroVentas.objects.all()
    registros_hoy = RegistroVentas.objects.filter(fecha=timezone.now().today())    
    venta_total =sum([registro.calcular_total_ventas() for registro in registros_hoy])
    return render(request, 'resumen_ventas_totales.html', {'venta_total': venta_total, 'registros': registros})




