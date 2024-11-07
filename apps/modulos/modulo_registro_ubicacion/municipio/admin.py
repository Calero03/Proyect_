from django.contrib import admin

# Register your models here.
from apps.modulos.modulo_registro_ubicacion.municipio.models import Municipio

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ['id_municipio', 'nombre_municipio']
    list_display = ['id_municipio', 'departamento', 'nombre_municipio']
