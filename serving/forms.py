from django import forms
from .models import UnidadModel, ArticuloModel


class  FormUnidad(forms.ModelForm):
  class Meta:
    model = UnidadModel
    fields=['nombreUnidad', 'tipo', 'telefono', 'ubicacion', 'descripcion', 'correo', 'comandante']
    
class  FormArticulo(forms.ModelForm):
  class Meta:
    model = ArticuloModel
    fields=['descripcionGeneral', 'marca', 'modelo', 'serial', 'unidad' , 'cantidad']