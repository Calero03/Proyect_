from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.exceptions import NotFound
from apps.seguridad.permissions import *
from rest_framework.permissions import IsAuthenticated

from .models import Proveedor
from .serializers import ProveedorSerializers


class ProveedorApiView(APIView):
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Proveedor


    @swagger_auto_schema(
        responses={200: ProveedorSerializers(many=True)},
        operation_description="Obtiene una lista de todos los proveedores."
    )
    def get(self, request):
        proveedores = Proveedor.objects.all()
        serializer = ProveedorSerializers(proveedores, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=ProveedorSerializers,
        responses={201: ProveedorSerializers},
        operation_description="Crea un nuevo proveedor."
    )
    def post(self, request):
        serializer = ProveedorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        request_body=ProveedorSerializers,
        responses={200: ProveedorSerializers},
        operation_description="Actualiza un proveedor existente."
    )
    def put(self, request, pk):
        try:
            proveedor = Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Proveedor no encontrado."})
        
        serializer = ProveedorSerializers(proveedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        responses={204: "Proveedor eliminado exitosamente.", 404: "Proveedor no encontrado."},
        operation_description="Elimina físicamente un proveedor de la base de datos."
    )
    def delete(self, request, pk):  
        try:
            proveedor = Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Proveedor no encontrado."})
        
        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "Proveedor eliminado exitosamente."})
