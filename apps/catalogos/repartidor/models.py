from django.db import models

# Create your models here.

class Repartidor(models.Model):
    id_repartidor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    cedula = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    numero_licencia = models.CharField(max_length=50, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Repartidores'

    def __str__(self):
        return f"ID: {self.id_repartidor}, Nombre: {self.nombre}, Estado: {'Activo' if self.estado else 'Inactivo'}"

