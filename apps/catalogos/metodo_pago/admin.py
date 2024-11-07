from django.contrib import admin

# Register your models here.
from apps.catalogos.metodo_pago.models import MetodoPago

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    search_fields = ['id_metodo_pago', 'nombre_metodo_pago', 'descripcion', 'fecha']
    list_display = ['id_metodo_pago', 'nombre_metodo_pago', 'descripcion', 'estado', 'fecha']
