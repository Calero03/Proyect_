from django.urls import path
from .views import ProductoApiView, ConteoProductoApiView
from .views import FiltrarProductoApiView
from .views import ListaEnlazadaApiView, TablaHashApiView
from .views import ProductoPrecioTotalView

app_name = "producto"

urlpatterns = [
    path('', ProductoApiView.as_view(), name="producto"),
    path('producto/<int:pk>/', ProductoApiView.as_view(), name='producto-detail'),
    path('producto/conteo/', ConteoProductoApiView.as_view(), name='conteo_productos'),
    path('producto/filtrar/', FiltrarProductoApiView.as_view(), name='filtrar_productos'),
    path('lista_enlazada/', ListaEnlazadaApiView.as_view(), name='producto-lista-enlazada'),
    path('tabla_hash/', TablaHashApiView.as_view(), name='producto-tabla-hash'),
    path('productos/calcular_precio/', ProductoPrecioTotalView.as_view(), name='calcular_precio_producto'),
]

