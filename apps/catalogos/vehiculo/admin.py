from django.contrib import admin

# Register your models here.
from apps.catalogos.vehiculo.models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    search_fields = ['id_vehiculo', 'tipo_vehiculo', 'capacidad']
    list_display = ['id_vehiculo', 'tipo_vehiculo', 'capacidad', 'consumo_combustible', 'estado']

