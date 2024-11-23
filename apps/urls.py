from django.urls import path, include

urlpatterns = [
    path('catalogos/', include('apps.catalogos.categoria.urls')),
    path('modulos/', include('apps.modulos.modulo_registro_facturacion.factura.urls')),
    path('departamento/', include('apps.catalogos.departamento.urls')),
    path('municipio/', include('apps.modulos.modulos_registro_ubicacion.municipio.urls')),
    path('producto/', include('apps.modulos.modulo_registro_producto.producto.urls')),
    path('repartidor/', include('apps.catalogos.repartidor.urls')),
    path('vehiculo/', include('apps.catalogos.vehiculo.urls')),
    path('envio/', include('apps.modulos.modulo_registro_envio.envio.urls')),
    path('cliente/', include('apps.modulos.modulo_registro_cliente.cliente.urls')),
    path('metodo_pago/', include('apps.catalogos.metodo_pago.urls')),
    path('proveedor/', include('apps.catalogos.proveedor.urls')),
    path('seguridad/', include('apps.seguridad.urls')),
]