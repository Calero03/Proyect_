from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.exceptions import NotFound

from .models import Departamento
from .serializers import DepartamentoSerializers

class DepartamentoApiView(APIView):

    @swagger_auto_schema(
        responses={200: DepartamentoSerializers(many=True)},
        operation_description="Obtiene una lista de todos los departamentos."
    )
    def get(self, request):
        departamentos = Departamento.objects.all()
        serializer = DepartamentoSerializers(departamentos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=DepartamentoSerializers,
        responses={201: DepartamentoSerializers},
        operation_description="Crea un nuevo departamento."
    )
    def post(self, request):
        serializer = DepartamentoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        request_body=DepartamentoSerializers,
        responses={200: DepartamentoSerializers},
        operation_description="Actualiza un departamento existente."
    )
    def put(self, request, pk):
        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Departamento no encontrado."})
        
        serializer = DepartamentoSerializers(departamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        responses={204: None},
        operation_description="Elimina un departamento."
    )
    def delete(self, request, pk):
        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Departamento no encontrado."})
        
        departamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
