from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.exceptions import NotFound

from .models import Repartidor
from .serializers import RepartidorSerializers


class RepartidorApiView(APIView):

    @swagger_auto_schema(
        responses={200: RepartidorSerializers(many=True)},
        operation_description="Obtiene una lista de todos los repartidores."
    )
    def get(self, request):
        repartidores = Repartidor.objects.all()
        serializer = RepartidorSerializers(repartidores, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=RepartidorSerializers,
        responses={201: RepartidorSerializers},
        operation_description="Crea un nuevo repartidor."
    )
    def post(self, request):
        serializer = RepartidorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        request_body=RepartidorSerializers,
        responses={200: RepartidorSerializers},
        operation_description="Actualiza un repartidor existente."
    )
    def put(self, request, pk):
        try:
            repartidor = Repartidor.objects.get(pk=pk)
        except Repartidor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Repartidor no encontrado."})
        
        serializer = RepartidorSerializers(repartidor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        responses={204: None},
        operation_description="Elimina un repartidor."
    )
    def delete(self, request, pk):
        try:
            repartidor = Repartidor.objects.get(pk=pk)
        except Repartidor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Repartidor no encontrado."})
        
        repartidor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
