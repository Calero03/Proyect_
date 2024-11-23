from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.exceptions import NotFound

from .models import Cliente
from .serializers import ClienteSerializers

class ClienteApiView(APIView):

    @swagger_auto_schema(
        responses={200: ClienteSerializers(many=True)},
        operation_description="Obtiene una lista de todos los clientes."
    )
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializers(clientes, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=ClienteSerializers,
        responses={201: ClienteSerializers},
        operation_description="Crea un nuevo cliente."
    )
    def post(self, request):
        serializer = ClienteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        request_body=ClienteSerializers,
        responses={200: ClienteSerializers},
        operation_description="Actualiza un cliente existente."
    )
    def put(self, request, pk):
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Cliente no encontrado."})
        
        serializer = ClienteSerializers(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        responses={204: None},
        operation_description="Elimina un cliente."
    )
    def delete(self, request, pk):
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Cliente no encontrado."})
        
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
