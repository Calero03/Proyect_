from rest_framework.serializers import ModelSerializer
from .models import Repartidor

class RepartidorSerializers(ModelSerializer):
    class Meta:
        model = Repartidor
        fields = ['nombre', 'cedula', 'telefono', 'numero_licencia']