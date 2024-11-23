from django.urls import path
from .views import EnvioApiView

app_name = "envio"

urlpatterns = [
    path('', EnvioApiView.as_view(), name="envio"),
    path('envio/<int:pk>/', EnvioApiView.as_view(), name='envio-detail'),
]
