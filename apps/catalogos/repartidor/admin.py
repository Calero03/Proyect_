from django.contrib import admin

# Register your models here.
from apps.catalogos.repartidor.models import Repartidor

@admin.register(Repartidor)
class RepartidorAdmin(admin.ModelAdmin):
    search_fields = ['id_repartidor', 'nombre', 'cedula']
    list_display = ['id_repartidor', 'nombre', 'cedula', 'telefono', 'direccion', 'numero_licencia', 'estado']

