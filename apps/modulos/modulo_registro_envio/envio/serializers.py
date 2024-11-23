from rest_framework.serializers import ModelSerializer
from .models import Envio

class EnvioSerializers(ModelSerializer):
    class Meta:
        model = Envio
        fields = ['fecha_envio', 'costo_envio', 'direccion', 'distancia_km']
