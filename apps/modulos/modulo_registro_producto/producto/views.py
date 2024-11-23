from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import Producto
from .serializers import ProductoSerializers

class ProductoApiView(APIView):

   
    @swagger_auto_schema(
        responses={200: ProductoSerializers(many=True)},
        operation_description="Obtiene una lista de todos los productos."
    )
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializers(productos, many=True)
        return Response(status=status.HTTP_200_OK,  data=serializer.data)

    
    @swagger_auto_schema(
        request_body=ProductoSerializers,
        responses={201: ProductoSerializers},
        operation_description="Crea un nuevo producto."
    )
    def post(self, request):
        serializer = ProductoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

   
    @swagger_auto_schema(
        request_body=ProductoSerializers,
        responses={200: ProductoSerializers},
        operation_description="Actualiza un producto existente."
    )
    def put(self, request, pk):
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Producto no encontrado."})

        serializer = ProductoSerializers(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    
    @swagger_auto_schema(
        responses={204: None},
        operation_description="Elimina un producto."
    )
    def delete(self, request, pk):
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Producto no encontrado."})

        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Filtrar productos por categoría o proveedor
class FiltrarProductoApiView(APIView):
    @swagger_auto_schema(
        responses={200: ProductoSerializers(many=True)},
        operation_description="Filtra productos por categoría o proveedor. Debes enviar 'id_categoria' o 'proveedor_id' como parámetros."
    )
    def get(self, request):
        id_categoria = request.query_params.get('id_categoria')
        id_proveedor = request.query_params.get('proveedor_id')

        if id_categoria:
            productos = Producto.objects.filter(categoria_id=id_categoria)
        elif id_proveedor:
            productos = Producto.objects.filter(proveedor_id=id_proveedor)
        else:
            return Response({"error": "Proporcione 'id_categoria' o 'proveedor_id' para filtrar."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductoSerializers(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    # Obtener el conteo de productos
class ConteoProductoApiView(APIView):
    @swagger_auto_schema(
        responses={200: "Conteo total de productos."},
        operation_description="Obtiene el conteo total de productos registrados."
    )
    def get(self, request):
        total_productos = Producto.objects.count()
        return Response({"total_productos": total_productos}, status=status.HTTP_200_OK)
