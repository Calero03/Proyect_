from rest_framework.serializers import ModelSerializer
from .models import Vehiculo

class VehiculoSerializers(ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['tipo_vehiculo', 'capacidad', 'consumo_combustible', 'estado']