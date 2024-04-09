from django.db import models
from django.urls import reverse
import random


class UnidadModel(models.Model):
  code = models.CharField(max_length=100, unique=True)
  descripcion = models.TextField(null=True)
  ubicacion = models.TextField(null=True)
  telefono = models.CharField(max_length=200, verbose_name="telefono")
  correo = models.EmailField()
  tipo = models.CharField(max_length=200, verbose_name="Tipo")
  nombreUnidad = models.CharField(max_length=200, verbose_name="Nombre de la Unidad")
  comandante = models.CharField(max_length=200, verbose_name="Comandante")
  
  def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_unique_code()
        super().save(*args, **kwargs)
    
  @staticmethod
  def generate_unique_code():
      prefix = 'SERVING'
      while True:
          suffix = ''.join(str(random.randint(0, 9)) for _ in range(6))
          code = f'{prefix}{suffix}'
          if not UnidadModel.objects.filter(code=code).exists():
              return code
  
  def  __str__(self):
    return f'{self.nombreUnidad} - {self.tipo} - {self.telefono}- {self.comandante}'
  
  def get_absolute_url(self):
        return reverse("servicio")
    

class ArticuloModel(models.Model):
  code = models.CharField(max_length=100, verbose_name="Codigo de Equipo")
  descripcionGeneral = models.TextField()
  marca = models.CharField(max_length=200)
  modelo = models.CharField(max_length=200)
  serial = models.CharField(max_length=200)
  fechaIngreso = models.DateField(auto_now_add=True)
  cantidad = models.IntegerField(default=0)

  unidad = models.ForeignKey(UnidadModel, on_delete=models.CASCADE)
  
  def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_unico_code()
        super().save(*args, **kwargs)
    
  @staticmethod
  def generate_unico_code():
      prefix = 'MTEQ'
      while True:
          suffix = ''.join(str(random.randint(0, 9)) for _ in range(6))
          code = f'{prefix}{suffix}'
          if not UnidadModel.objects.filter(code=code).exists():
              return code
  
  def  __str__(self):
    return f'{self.descripcionGeneral} - {self.marca} - {self.modelo}- {self.serial}'
  

  
  
  

  
  
  
