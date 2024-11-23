from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.exceptions import NotFound

from .models import Vehiculo
from .serializers import VehiculoSerializers


class VehiculoApiView(APIView):

    @swagger_auto_schema(
        responses={200: VehiculoSerializers(many=True)},
        operation_description="Obtiene una lista de todos los vehículos."
    )
    def get(self, request):
        vehiculos = Vehiculo.objects.all()
        serializer = VehiculoSerializers(vehiculos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=VehiculoSerializers,
        responses={201: VehiculoSerializers},
        operation_description="Crea un nuevo vehículo."
    )
    def post(self, request):
        serializer = VehiculoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        request_body=VehiculoSerializers,
        responses={200: VehiculoSerializers},
        operation_description="Actualiza un vehículo existente."
    )
    def put(self, request, pk):
        try:
            vehiculo = Vehiculo.objects.get(pk=pk)
        except Vehiculo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Vehículo no encontrado."})
        
        serializer = VehiculoSerializers(vehiculo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


    @swagger_auto_schema(
        responses={200: "Vehículo anulado exitosamente.", 404: "Vehículo no encontrado."},
        operation_description="Anula un vehículo marcando su estado como inactivo (False)."
    )
    def delete(self, request, pk):
        try:
            vehiculo = Vehiculo.objects.get(pk=pk)
        except Vehiculo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Vehículo no encontrado."})
        
        # Anular vehículo cambiando su estado
        vehiculo.estado = False
        vehiculo.save()
        return Response(status=status.HTTP_200_OK, data={"message": "Vehículo anulado exitosamente."})

