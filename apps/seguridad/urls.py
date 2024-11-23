from django.urls import path, include

urlpatterns = [
    path('usuario/', include('apps.seguridad.usuario.urls')),
]