from django.db import models

# Create your models here.

class Departamento(models.Model):
    nombre_departamento = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre_departamento}"

