from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Unidad, Articulo, ArticuloUnidad
from .forms import FormUnidad , FormArticulo, FormEnvio

# vista de inventario

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
 

class EditarVista(UpdateView):
    model = Articulo
    form_class = FormArticulo
    template_name = "articulos/editar.html"
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object() 
        return super().get(request, self.template_name, *args, **kwargs)
    
    def get_initial(self):
        initial = super().get_initial()
        #initial['serial'] = self.object.serial
        return initial
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect('articulos')
      
  
class EliminarVista(DeleteView):
  model = Articulo
  template_name = "articulos/eliminar.html"
  success_url = reverse_lazy('articulos')
  
  # ---------- fin de la vista inventario
  
  
  
  # inicio de la vista de envio de articulos

class VistaEnvio(CreateView):
    form_class = FormEnvio
    initial = {"key": "value"}
    template_name = "envios/envio_articulo.html"

    def get(self, request, *args, **kwargs):
        articulo = Articulo.objects.all()
        unidad = Unidad.objects.all()
        context = {'articulo': articulo, 'unidad': unidad}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        formulario_envio = self.form_class(request.POST)
        if formulario_envio.is_valid():
            articulo = formulario_envio.cleaned_data['articulo']
            unidad = formulario_envio.cleaned_data['unidad']
            cantidad = formulario_envio.cleaned_data['cantidad']
            if articulo.cantidad >= cantidad:
                articulo.cantidad -= cantidad
                articulo.save()
                ArticuloUnidad.objects.create(
                    movimiento='Envío',
                    articulo=articulo,
                    unidad=unidad,
                    cantidad=cantidad,
                    precio=articulo.precio,
                    serial =articulo.serial
                )
                return redirect('articulos')
            else:
              return redirect('saldo insuficiente')
              
        context = {'formulario_envio': formulario_envio}
        return render(request, self.template_name, context)
        
# fin de la vista de articulos 


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
    unidad= Unidad.objects.get(pk=id)
    articulo = ArticuloUnidad.objects.filter(unidad=unidad)
    context={'articulo':articulo}
    return render(request, 'subunidad/unidad_articulo.html',context)
  
  
class EditarVistaUnidad(UpdateView):
    model = Unidad
    form_class = FormUnidad
    template_name = "unidad/editar_unidad.html"
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object() 
        return super().get(request, self.template_name, *args, **kwargs)
    
    def get_initial(self):
        initial = super().get_initial()
        return initial
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect('unidad')
      
      
class EliminarVistaUnidad(DeleteView):
  model = Unidad
  template_name = "unidad/eliminar_unidad.html"
  success_url = reverse_lazy('unidad')
  
