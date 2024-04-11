from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from . import views
from serving.views import VistaPrincipal, VistaCrear, Actualizar, Eliminar, VistaArticulo, CrearArticulo


urlpatterns = [
    path("", VistaPrincipal.as_view(), name="servicio"),
    path("servicio/crear", VistaCrear.as_view(), name="crear"),
    path("servicio/<int:pk>/editar", Actualizar.as_view(), name="editar"),
    path("eliminar/<int:pk>", Eliminar.as_view(), name="eliminar"),
    
    
    #Rutas de los Articulos
    path("articulos/articulo_info/<int:id>", VistaArticulo.as_view(), name="articulo"),
    path("articulos/crear_articulo/<int:id>", CrearArticulo.as_view(), name="crear_articulo"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)