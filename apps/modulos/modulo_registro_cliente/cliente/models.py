from django.db import models

# Create your models here.
from apps.modulos.modulo_registro_ubicacion.municipio.models import Municipio

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    cedula = models.CharField(max_length=50, unique=True)
    municipio = models.ForeignKey(Municipio, verbose_name='Municipio', on_delete=models.PROTECT)
    direccion_cliente = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"ID: {self.id_cliente}, Nombre: {self.nombre}, Municipio: {self.municipio.nombre_municipio}"
