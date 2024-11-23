from rest_framework.serializers import ModelSerializer
from .models import MetodoPago

class MetodoPagoSerializers(ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = ['nombre_metodo_pago', 'descripcion', 'estado', 'fecha']
