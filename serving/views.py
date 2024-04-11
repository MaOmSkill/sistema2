from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Unidad, Articulo
from .forms import FormUnidad , FormArticulo


class VistaInventario(View):
  
  def get(self, request, *args, **kwargs):
    articulo = Articulo.objects.all()
    unidades = Unidad.objects.all().count()
    context = {'articulo':articulo, 'unidades':unidades}
    return render(request, 'articulos/index.html', context)
  

class CrearArticulo(CreateView):
  form_class = FormArticulo
  initial = {"key": "value"}
  template_name = "articulos/crear.html"
  def get(self, request, *args, **kwargs):
    formulario_articulo = self.form_class(initial=self.initial)
    context = {'formulario_articulo':formulario_articulo}
    return render(request, self.template_name, context)
  
  def post(self, request, *args, **kwargs):
    formulario_articulo =self.form_class(request.POST)
    if formulario_articulo.is_valid():
      formulario_articulo.save()
      return redirect('articulos')
    return render(request, self.template_name, {'formulario_articulo':formulario_articulo})
  
    
class VistaEnvio(View):
  def get(self, request, *args, **kwargs):
    articulo = Articulo.objects.all()
    unidad = Unidad.objects.all()
    context = {'articulo':articulo, 'unidad':unidad}
    return render(request, 'envios/envio_articulo.html', context)

class VistaUnidad(View):
  
  def get(self, request, *args, **kwargs):
    unidad = Unidad.objects.all()
    context = {'unidad':unidad}
    return render(request, 'unidad/unidad_index.html',context)

class CrearUnidad(CreateView):
  form_class = FormUnidad
  initial = {"key": "value"}
  template_name = "unidad/crear_unidad.html"
  def get(self, request, *args, **kwargs):
    formulario_unidad = self.form_class(initial=self.initial)
    context = {'formulario_unidad':formulario_unidad}
    return render(request, self.template_name, context)
  
  def post(self, request, *args, **kwargs):
    formulario_unidad = self.form_class(request.POST)
    if formulario_unidad.is_valid():
      formulario_unidad.save()
      return redirect('unidad')
    return render(request, self.template_name, {'formulario_unidad':formulario_unidad})


class UnidadArticulo(View):
  
  def get(self, request, id):
    return render(request, 'subunidad/unidad_articulo.html')