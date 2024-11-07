from django.db import models

# Create your models here.

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    ruc = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return f"ID: {self.id_proveedor}, Nombre: {self.nombre}, RUC: {self.ruc}"
