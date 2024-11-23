from django.urls import path
from .views import ProveedorApiView

app_name = "Proveedor"

urlpatterns = [
    path('', ProveedorApiView.as_view(), name="proveedor"),
    path('proveedor/<int:pk>/', ProveedorApiView.as_view(), name='proveedor-detail'),
]
