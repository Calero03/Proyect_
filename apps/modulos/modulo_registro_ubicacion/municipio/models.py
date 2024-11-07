from django.db import models

# Create your models here.
from apps.catalogos.departamento.models import Departamento

class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    departamento = models.ForeignKey(Departamento, verbose_name='Departamento', on_delete=models.PROTECT)
    nombre_municipio = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return f"ID: {self.id_municipio}, Departamento: {self.departamento.nombre_departamento}, Nombre: {self.nombre_municipio}"