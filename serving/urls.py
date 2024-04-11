from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from serving.views import VistaInventario, CrearArticulo, VistaEnvio, VistaUnidad, CrearUnidad, UnidadArticulo


urlpatterns = [
     path("", VistaInventario.as_view(), name="articulos"),
     path("articulo/crear.html", CrearArticulo.as_view(), name="crear_articulo"),
     path("envios/envio_articulo", VistaEnvio.as_view(), name="envio_articulo"),
     path("unidad/unidad_index", VistaUnidad.as_view(), name="unidad"),
     path("unidad/crear_unidad", CrearUnidad.as_view(), name="crear_unidad"),
     path("subunidad/unidad_articulo/<int:id>", UnidadArticulo.as_view(), name="unidad_articulo"),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)