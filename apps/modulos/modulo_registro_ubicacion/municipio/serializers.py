from rest_framework.serializers import ModelSerializer
from .models import Municipio

class MunicipioSerializers(ModelSerializer):
    class Meta:
        model = Municipio
        fields = ['id_municipio', 'departamento', 'nombre_municipio']