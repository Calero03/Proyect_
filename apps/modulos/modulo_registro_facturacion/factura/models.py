from django.db import models

# Create your models here.
from apps.modulos.modulo_registro_cliente.cliente.models import Cliente
from apps.catalogos.metodo_pago.models import MetodoPago
from apps.modulos.modulo_registro_producto.producto.models import Producto

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.PROTECT)
    fecha_factura = models.DateField()
    metodo_pago = models.ForeignKey(MetodoPago, verbose_name='Método de Pago', on_delete=models.PROTECT)
    estado_factura = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, help_text="Precio del producto en el momento de la compra")
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, default=1)

    class Meta:
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return f"ID: {self.id_factura}, Cliente: {self.cliente.nombre}, Método de Pago: {self.metodo_pago.nombre_metodo_pago}, Estado: {'Activo' if self.estado_factura else 'Inactivo'}, Producto: {self.producto.nombre_producto}"