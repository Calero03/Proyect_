from django.urls import path
from .views import MunicipioApiView

app_name = "municipio"

urlpatterns = [
    path('', MunicipioApiView.as_view(), name="municipio"),
    path('municipio/<int:pk>/', MunicipioApiView.as_view(), name='municipio-detail'),
]
