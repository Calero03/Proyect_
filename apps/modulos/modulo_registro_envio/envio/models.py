from django.db import models

# Create your models here.
from apps.modulos.modulo_registro_facturacion.factura.models import Factura
from apps.catalogos.vehiculo.models import Vehiculo
from apps.catalogos.repartidor.models import Repartidor

class Envio(models.Model):
    id_envio = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, verbose_name='Factura', on_delete=models.PROTECT)
    fecha_envio = models.DateField()
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    direccion = models.CharField(max_length=255)
    vehiculo = models.ForeignKey(Vehiculo, verbose_name='Vehículo', on_delete=models.PROTECT)
    repartidor = models.ForeignKey(Repartidor, verbose_name='Repartidor', on_delete=models.PROTECT)
    distancia_km = models.DecimalField(max_digits=10, decimal_places=2, help_text="Distancia en kilómetros")

    class Meta:
        verbose_name_plural = 'Envios'

    def __str__(self):
        return f"ID: {self.id_envio}, Factura: {self.factura.id_factura}, Vehículo: {self.vehiculo.tipo_vehiculo}, Repartidor: {self.repartidor.nombre}"

