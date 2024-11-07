from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField()

    class Meta:
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return f"ID: {self.id_categoria}, Nombre: {self.nombre_categoria}, Fecha: {self.fecha}"

