from django.urls import path
from .views import ClienteApiView

app_name = "cliente"

urlpatterns = [
    path('', ClienteApiView.as_view(), name="cliente"),
    path('cliente/<int:pk>/', ClienteApiView.as_view(), name='cliente-detail'),
]
