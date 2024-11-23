from django.urls import path
from .views import CategoriaApiView

app_name = "categoria"

urlpatterns = [
    path('', CategoriaApiView.as_view(), name="categoria"),
]
