from django.db import models

# Create your models here.

class MetodoPago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    nombre_metodo_pago = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Metodos de Pago'

    def __str__(self):
        return f"ID: {self.id_metodo_pago}, Nombre: {self.nombre_metodo_pago}, Estado: {'Activo' if self.estado else 'Inactivo'}"
