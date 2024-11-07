from django.contrib import admin

# Register your models here.
from apps.catalogos.departamento.models import Departamento

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre_departamento']
    list_display = ['nombre_departamento']