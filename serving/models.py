from django.db import models

class Articulo(models.Model):
  grupo = models.IntegerField(default=0)
  subgrupo = models.IntegerField(default=0)
  seccion = models.IntegerField(default=0)
  articulo = models.TextField()
  serial = models.CharField(max_length=200, verbose_name="Serial")
  unidad_medida = models.CharField(max_length=100, verbose_name="Unidad de Medida")
  fecha= models.DateField(auto_now_add=True)
  cantidad = models.IntegerField(default=0)
  precio = models.DecimalField(max_digits=6, decimal_places=2)
  
  def  __str__(self):
    return f'{self.articulo}-{self.unidad_medida}'
  
  def total(self):
    return self.cantidad * self.precio
  
  
  
class Unidad(models.Model):
  nombreUnidad = models.CharField(max_length=200, verbose_name="Nombre de la Unidad")
  comandante = models.CharField(max_length=200, verbose_name="Comandante")
  ubicacion = models.TextField(null=True)
  telefono = models.CharField(max_length=200, verbose_name="telefono")
  articulo = models.ManyToManyField(Articulo)

  def  __str__(self):
    return f'{self.nombreUnidad} - {self.telefono}- {self.comandante}'

  
  
