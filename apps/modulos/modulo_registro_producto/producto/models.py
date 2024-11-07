from django.db import models

# Create your models here.
from apps.catalogos.proveedor.models import Proveedor
from apps.catalogos.categoria.models import Categoria

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(Proveedor, verbose_name='Proveedor', on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoría', on_delete=models.PROTECT)
    nombre_producto = models.CharField(max_length=255)
    descripcion_producto = models.TextField(blank=True, null=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio del producto por unidad (ej. 15.50)")
    cantidad = models.IntegerField(default=0)
    dimensiones = models.CharField(max_length=255, blank=True, null=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, help_text="Peso en kg")
    marca = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre_producto}, Proveedor: {self.proveedor.nombre}, Categoría: {self.categoria.nombre_categoria}"
