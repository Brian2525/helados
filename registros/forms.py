
from django import forms
from productos.models import Producto
from sucursales.models import Sucursal
from personal.models import Personal

class RegistroDiarioTodosProductosForm(forms.Form):
    sucursal = forms.ModelChoiceField(
        queryset=Sucursal.objects.all(),
        label="Sucursal",
        required=True
    )
    personal = forms.ModelChoiceField(
        queryset=Personal.objects.all(),
        label="Personal",
        required=True
    )

    fecha = forms.DateField(
        label="Fecha del registro",
        widget=forms.DateInput(attrs={'type': 'date'})  # Esto renderiza un selector de fecha en HTML5
    )
    

    descripcion_gasto = forms.CharField(max_length=255, label="Descripción del Gasto", required=False)
    monto_gasto = forms.DecimalField(max_digits=10, decimal_places=2, label="Monto del Gasto", required=False)
    
    def __init__(self, *args, **kwargs):
        super(RegistroDiarioTodosProductosForm, self).__init__(*args, **kwargs)
        productos = Producto.objects.all()
        for producto in productos:
            # Agregamos un conjunto de campos por cada producto
            self.fields[f'inventario_inicial_{producto.id}'] = forms.IntegerField(label=f'Inventario inicial de {producto.nombre}', min_value=0)
            self.fields[f'llegada_mercancia_{producto.id}'] = forms.IntegerField(label=f'Llegada de mercancía de {producto.nombre}', min_value=0)
            self.fields[f'mercancia_defectuosa_{producto.id}'] = forms.IntegerField(label=f'Mercancía defectuosa de {producto.nombre}', min_value=0)
            self.fields[f'mercancia_sobrante_{producto.id}'] = forms.IntegerField(label=f'Mercancía sobrante de {producto.nombre}', min_value=0)
