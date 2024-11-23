from django.urls import path
from .views import FacturaApiView
from .views import BusquedaAvanzadaFacturasApiView
from .views import FacturasAnuladasApiView

app_name = "factura"

urlpatterns = [
    path('', FacturaApiView.as_view(), name="factura"),
    path('factura/<int:pk>/', FacturaApiView.as_view(), name='factura-detail'),
    path('facturas/busqueda-avanzada/', BusquedaAvanzadaFacturasApiView.as_view(), name='busqueda-avanzada-facturas'),
    path('facturas/anuladas/', FacturasAnuladasApiView.as_view(), name='facturas-anuladas'),
]
