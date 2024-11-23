from django.urls import path
from .views import DepartamentoApiView

app_name = "departamento"

urlpatterns = [
    path('', DepartamentoApiView.as_view(), name="departemento"),
    path('departamento/<int:pk>/', DepartamentoApiView.as_view(), name='departamento-detail'),
]
