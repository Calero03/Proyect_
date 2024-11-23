from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.exceptions import NotFound

from .models import Municipio
from .serializers import MunicipioSerializers

class MunicipioApiView(APIView):

    @swagger_auto_schema(
        responses={200: MunicipioSerializers(many=True)},
        operation_description="Obtiene una lista de todos los municipios."
    )
    def get(self, request):
        municipios = Municipio.objects.all()
        serializer = MunicipioSerializers(municipios, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=MunicipioSerializers,
        responses={201: MunicipioSerializers},
        operation_description="Crea un nuevo municipio."
    )
    def post(self, request):
        serializer = MunicipioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        request_body=MunicipioSerializers,
        responses={200: MunicipioSerializers},
        operation_description="Actualiza un municipio existente."
    )
    def put(self, request, pk):
        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Municipio no encontrado."})
        
        serializer = MunicipioSerializers(municipio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        responses={204: None},
        operation_description="Elimina un municipio."
    )
    def delete(self, request, pk):
        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Municipio no encontrado."})
        
        municipio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

