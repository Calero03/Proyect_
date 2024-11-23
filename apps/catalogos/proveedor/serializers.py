from rest_framework.serializers import ModelSerializer
from .models import Proveedor

class ProveedorSerializers(ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'ruc', 'direccion', 'telefono']
