from django.urls import path
from .views import ProductoApiView, ConteoProductoApiView, FiltrarProductoApiView

app_name = "producto"

urlpatterns = [
    path('', ProductoApiView.as_view(), name="producto"),
    path('producto/<int:pk>/', ProductoApiView.as_view(), name='producto-detail'),
    path('producto/conteo/', ConteoProductoApiView.as_view(), name='conteo_productos'),
    path('producto/filtrar/', FiltrarProductoApiView.as_view(), name='filtrar_productos'),
]

