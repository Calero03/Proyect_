from django.contrib import admin

# Register your models here.
from apps.catalogos.categoria.models import Categoria

@admin.register(Categoria)
class VehiculoAdmin(admin.ModelAdmin):
    search_fields = ['+id_categoria', 'nombre_categoria', 'descripcion']
    list_display = ['id_categoria', 'nombre_categoria', 'descripcion', 'fecha']
