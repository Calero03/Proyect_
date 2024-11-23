from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.exceptions import NotFound

from .models import MetodoPago
from .serializers import MetodoPagoSerializers


class MetodoPagoApiView(APIView):

    @swagger_auto_schema(
        responses={200: MetodoPagoSerializers(many=True)},
        operation_description="Obtiene una lista de todos los métodos de pago."
    )
    def get(self, request):
        metodos = MetodoPago.objects.all()
        serializer = MetodoPagoSerializers(metodos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=MetodoPagoSerializers,
        responses={201: MetodoPagoSerializers},
        operation_description="Crea un nuevo método de pago."
    )
    def post(self, request):
        serializer = MetodoPagoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        request_body=MetodoPagoSerializers,
        responses={200: MetodoPagoSerializers},
        operation_description="Actualiza un método de pago existente."
    )
    def put(self, request, pk):
        try:
            metodo = MetodoPago.objects.get(pk=pk)
        except MetodoPago.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Método de pago no encontrado."})
        
        serializer = MetodoPagoSerializers(metodo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        operation_description="Anula (desactiva) un método de pago en lugar de eliminarlo.",
        responses={200: "Método de pago desactivado exitosamente.", 404: "Método de pago no encontrado."}
    )
    def delete(self, request, pk):
        try:
            metodo = MetodoPago.objects.get(pk=pk)
        except MetodoPago.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Método de pago no encontrado."})
        
        metodo.estado = False
        metodo.save()
        return Response(status=status.HTTP_200_OK, data={"message": "Método de pago desactivado exitosamente."})
