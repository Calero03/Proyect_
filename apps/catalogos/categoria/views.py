from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


from .models import Categoria
from .serializers import CategoriaSerializers


class CategoriaApiView(APIView):

    @swagger_auto_schema(
        responses={200: CategoriaSerializers(many=True)},
        operation_description="Obtiene una lista de todas las categorías."
    )
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializers(categorias, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=CategoriaSerializers,
        responses={201: CategoriaSerializers},
        operation_description="Crea una nueva categoría."
    )
    def post(self, request):
        serializer = CategoriaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        request_body=CategoriaSerializers,
        responses={200: CategoriaSerializers},
        operation_description="Actualiza una categoría existente."
    )
    def put(self, request, pk):
        try:
            categoria = Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Categoría no encontrada."})
        
        serializer = CategoriaSerializers(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        responses={204: "Categoría eliminada exitosamente.", 404: "Categoría no encontrada."},
        operation_description="Elimina físicamente una categoría de la base de datos."
    )
    def delete(self, request, pk):
        try:
            categoria = Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Categoría no encontrada."})
        
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "Categoría eliminada exitosamente."})
