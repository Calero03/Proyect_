from django.urls import path
from .views import RepartidorApiView

app_name = "repartidor"

urlpatterns = [
    path('', RepartidorApiView.as_view(), name="repartidor"),
    path('repartidor/<int:pk>/', RepartidorApiView.as_view(), name='repartidor-detail'),
]
