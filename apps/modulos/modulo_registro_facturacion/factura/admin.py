from django.contrib import admin

# Register your models here.
from apps.modulos.modulo_registro_facturacion.factura.models import Factura

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    search_fields = ['id_factura', 'cliente', 'fecha_factura']
    list_display = ['id_factura', 'cliente', 'fecha_factura', 'metodo_pago', 'estado_factura', 'descripcion', 'cantidad', 'precio_unitario', 'producto']