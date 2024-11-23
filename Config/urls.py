"""
URL configuration for Config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Sistema API",
      default_version='v1',
      description="API para la gestión de facturas en el sistema.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('categoria/', include('apps.catalogos.categoria.urls')), 
    path('factura/', include('apps.modulos.modulo_registro_facturacion.factura.urls')),
    path('departamento/', include('apps.catalogos.departamento.urls')),
    path('municipio/', include('apps.modulos.modulo_registro_ubicacion.municipio.urls')),
    path('producto/', include('apps.modulos.modulo_registro_producto.producto.urls')),
    path('repartidor/', include('apps.catalogos.repartidor.urls')),
    path('vehiculo/', include('apps.catalogos.vehiculo.urls')),
    path('envio/', include('apps.modulos.modulo_registro_envio.envio.urls')),
    path('cliente/', include('apps.modulos.modulo_registro_cliente.cliente.urls')),
    path('metodo_pago/', include('apps.catalogos.metodo_pago.urls')),
    path('proveedor/', include('apps.catalogos.proveedor.urls')),
    path('seguridad/', include('apps.seguridad.urls')),
]
