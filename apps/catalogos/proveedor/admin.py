from django.contrib import admin

# Register your models here.
from apps.catalogos.proveedor.models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    search_fields = ['id_proveedor', 'nombre', 'ruc']
    list_display = ['id_proveedor', 'nombre', 'ruc', 'direccion', 'telefono']
