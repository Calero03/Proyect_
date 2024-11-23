from rest_framework.serializers import ModelSerializer
from .models import Cliente

class ClienteSerializers(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id_cliente', 'nombre', 'cedula', 'direccion_cliente', 'telefono', 'email', 'municipio']

    # VALIDACION DE LA CEDULA (SI ES NECESARIO)
    def validate_cedula(self, value):
        if len(value) != 14:
            raise serializers.ValidationError("La cédula debe tener al menos 10 caracteres.")
        return value
