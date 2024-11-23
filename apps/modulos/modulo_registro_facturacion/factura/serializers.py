from rest_framework.serializers import ModelSerializer
from .models import Factura

class FacturaSerializers(ModelSerializer):
    class Meta:
        model = Factura
        fields = ['cliente', 'id_factura', 'fecha_factura', 'descripcion', 'cantidad', 'producto', 'metodo_pago', 'estado_factura']
