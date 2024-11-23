from django.urls import path
from .views import MetodoPagoApiView

app_name = "MetodoPago"

urlpatterns = [
    path('', MetodoPagoApiView.as_view(), name="metodo_pago"),
    path('metodo_pago/<int:pk>/', MetodoPagoApiView.as_view(), name='metodo_pago-detail'),
]
