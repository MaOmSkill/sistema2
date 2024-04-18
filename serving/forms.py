from django import forms
from .models import Unidad, Articulo, ArticuloUnidad


class  FormUnidad(forms.ModelForm):
  class Meta:
    model = Unidad
    fields=['nombreUnidad', 'telefono', 'ubicacion', 'comandante']
    
class  FormArticulo(forms.ModelForm):
  class Meta:
    model = Articulo
    fields=['articulo', 'cantidad', 'precio' ,'grupo' ,'subgrupo' ,'seccion' ,'unidad_medida', 'serial']
    
class FormEnvio(forms.ModelForm):
    class Meta:
        model = ArticuloUnidad
        fields = ['articulo', 'unidad', 'cantidad']