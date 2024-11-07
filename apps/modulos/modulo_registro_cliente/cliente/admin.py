from django.contrib import admin

# Register your models here.
from apps.modulos.modulo_registro_cliente.cliente.models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['id_cliente', 'nombre', 'cedula', 'municipio']
    list_display = ['id_cliente', 'nombre', 'cedula', 'municipio', 'direccion_cliente', 'telefono', 'email']