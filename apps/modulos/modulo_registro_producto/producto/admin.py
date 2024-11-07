from django.contrib import admin

# Register your models here.
from apps.modulos.modulo_registro_producto.producto.models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['id_producto', 'proveedor', 'categoria', 'nombre_producto', 'descripcion_producto']
    list_display = ['id_producto', 'proveedor', 'categoria', 'nombre_producto', 'descripcion_producto', 'precio_unitario', 'cantidad', 'dimensiones', 'peso', 'marca']
