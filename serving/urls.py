from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from serving.views import (
    VistaInventario,
    CrearArticulo,
    VistaEnvio,
    VistaUnidad,
    CrearUnidad,
    UnidadArticulo,
    EditarVista,
    EliminarVista,
    EditarVistaUnidad,
    EliminarVistaUnidad,
)


urlpatterns = [
    path("", VistaInventario.as_view(), name="articulos"),
    path("articulos/crear.html", CrearArticulo.as_view(), name="crear_articulo"),
    path("articulos/editar/<int:pk>", EditarVista.as_view(), name="editar"),
    path("articulos/<int:pk>/eliminar/", EliminarVista.as_view(), name="eliminar"),
    # envios
    path("envios/envio_articulo", VistaEnvio.as_view(), name="envio_articulo"),
    # Unidad
    path("unidad/unidad_index", VistaUnidad.as_view(), name="unidad"),
    path("unidad/crear_unidad", CrearUnidad.as_view(), name="crear_unidad"),
    path(
        "unidad/editar_unidad/<int:pk>",
        EditarVistaUnidad.as_view(),
        name="editar_unidad",
    ),
    path(
        "unidad/<int:pk>/editar_unidad/",
        EliminarVistaUnidad.as_view(),
        name="eliminar_unidad",
    ),
    # subunidades
    path(
        "subunidad/unidad_articulo/<int:id>",
        UnidadArticulo.as_view(),
        name="unidad_articulo",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
