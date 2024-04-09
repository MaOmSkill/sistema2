from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import UnidadModel, ArticuloModel
from .forms import FormUnidad , FormArticulo


class VistaPrincipal(View):
  def get(self, request):
    servicio = UnidadModel.objects.all()
    context = {'servicio':servicio}
    return render(request,'servicio/index.html',context)
  
class VistaCrear(CreateView):
  form_class = FormUnidad
  initial = {"key": "value"}
  template_name="servicio/crear.html"
  
  def get(self, request, *args, **kwargs):
    form = self.form_class(initial=self.initial)
    return render(request, self.template_name, {'form': form})
  
  
  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    if form.is_valid():
      form.save()
      return redirect('servicio')
    return render(request, self.template_name, {'form': form})
  
class Actualizar(UpdateView):
    model = UnidadModel
    template_name = "servicio/editar.html" 
    fields=['nombreUnidad', 'tipo', 'telefono', 'ubicacion', 'descripcion', 'correo', 'comandante']
    
class Eliminar(DeleteView):
    model = UnidadModel
    success_url = reverse_lazy('servicio')
    template_name = "servicio/unidadmodel_confirm_delete.html"
    success_message = 'Identificador %(nombreUnidad)s Eliminado'
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message % self.get_object())
        return super().delete(request, *args, **kwargs)
      
      
# Vistas de los Artículos
class VistaArticulo(View):
    def get(self, request, id):
        articulos = ArticuloModel.objects.filter(pk=id)
        return render(request, 'articulos/articulo_info.html', {'articulos':articulos})

class CrearArticulo(CreateView):
    form_class = FormArticulo
    initial = {"key": "value"}
    template_name = "articulos/crear_articulo.html"

    def get(self, request, id):
        unidad = UnidadModel.objects.filter(pk=id)
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'unidad': unidad})

    def post(self, request, id):
        form = self.form_class(request.POST)
        if form.is_valid():
          nuevo =form.save()
          id = nuevo.unidad.id
          return redirect('articulo', id=id)
        return render(request, self.template_name, {'form': form})


