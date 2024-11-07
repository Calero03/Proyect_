from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    tipo_vehiculo = models.CharField(max_length=100)
    capacidad = models.DecimalField(max_digits=10, decimal_places=2, help_text="Capacidad en unidades (ej. toneladas, m³)")
    consumo_combustible = models.DecimalField(max_digits=10, decimal_places=2, help_text="Consumo de combustible en km/l")
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Vehículos'

    def __str__(self):
        return f"ID: {self.id_vehiculo}, Tipo: {self.tipo_vehiculo}, Estado: {'Activo' if self.estado else 'Inactivo'}"
