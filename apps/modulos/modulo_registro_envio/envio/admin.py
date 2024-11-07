from django.contrib import admin

# Register your models here.
from apps.modulos.modulo_registro_envio.envio.models import Envio

@admin.register(Envio)
class EnvioAdmin(admin.ModelAdmin):
    search_fields = ['id_envio', 'factura', 'fecha_envio']
    list_display = ['id_envio', 'factura', 'fecha_envio', 'costo_envio', 'direccion', 'vehiculo', 'repartidor', 'distancia_km']
