from django.urls import path
from .views import VehiculoApiView

app_name = "vehiculo"

urlpatterns = [
    path('', VehiculoApiView.as_view(), name="vehiculo"),
    path('vehiculo/<int:pk>/', VehiculoApiView.as_view(), name='vehiculo-detail'),
]
