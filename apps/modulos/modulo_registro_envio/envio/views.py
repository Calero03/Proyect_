from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.exceptions import NotFound

from .models import Envio
from .serializers import EnvioSerializers


class EnvioApiView(APIView):

    @swagger_auto_schema(
        responses={200: EnvioSerializers(many=True)},
        operation_description="Obtiene una lista de todos los envíos."
    )
    def get(self, request):
        envios = Envio.objects.all()
        serializer = EnvioSerializers(envios, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=EnvioSerializers,
        responses={201: EnvioSerializers},
        operation_description="Crea un nuevo envío."
    )
    def post(self, request):
        serializer = EnvioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        request_body=EnvioSerializers,
        responses={200: EnvioSerializers},
        operation_description="Actualiza un envío existente."
    )
    def put(self, request, pk):
        try:
            envio = Envio.objects.get(pk=pk)
        except Envio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Envío no encontrado."})
        
        serializer = EnvioSerializers(envio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        responses={204: None},
        operation_description="Elimina un envío."
    )
    def delete(self, request, pk):
        try:
            envio = Envio.objects.get(pk=pk)
        except Envio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Envío no encontrado."})
        
        envio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

