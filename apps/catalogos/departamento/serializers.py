from rest_framework.serializers import ModelSerializer
from .models import Departamento

class DepartamentoSerializers(ModelSerializer):
    class Meta:
        model = Departamento
        #fields = ['id', 'nombre_departamento']
        fields = '__all__'
