from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import Producto
from .serializers import ProductoSerializers
from .listas_enlazadas import ListaEnlazada, HashTable
from decimal import Decimal
from rest_framework.exceptions import NotFound
from apps.seguridad.permissions import *
from rest_framework.permissions import IsAuthenticated

class ProductoApiView(APIView):
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Producto

   
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
        #PERMISO...
        if not request.user.has_perm(f'{self.model._meta.app_label}.add_{self.model._meta.model_name}'):
            return Response(
                {"detail": "No tiene permiso para realizar esta acción."},
                status=status.HTTP_403_FORBIDDEN
            )
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
        
        #PEERMISOS...
        if not request.user.has_perm(f'{producto._meta.app_label}.change_{producto._meta.model_name}'):
            return Response(
                {"detail": "No tiene permiso para realizar esta acción."},
                status=status.HTTP_403_FORBIDDEN
            )

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



class ListaEnlazadaApiView(APIView):

    lista_enlazada = ListaEnlazada()

    @swagger_auto_schema(
        responses={200: ProductoSerializers(many=True)},
        operation_description="Obtiene los productos almacenados en la lista enlazada."
    )
    def get(self, request):
        
        productos = self.lista_enlazada.recorrer()

        
        if not productos:
            productos = Producto.objects.all()
            for producto in productos:
                self.lista_enlazada.agregar(producto)  

        # Serializar los productos
        serializer = ProductoSerializers(productos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)



class TablaHashApiView(APIView):

    tabla_hash = HashTable()

    @swagger_auto_schema(
        responses={200: ProductoSerializers(many=True)},
        operation_description="Obtiene los productos almacenados en la tabla hash."
    )
    def get(self, request):
        
        productos = []

        for index, bucket in enumerate(self.tabla_hash.table):
            if bucket:
                for producto in bucket:
                    productos.append(producto)

        
        if not productos:
            productos = Producto.objects.all()
            for producto in productos:
                self.tabla_hash.insertar(producto)  

        serializer = ProductoSerializers(productos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    



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
    


    #NNn
class ProductoPrecioTotalView(APIView):
    
    @swagger_auto_schema(
        request_body=ProductoSerializers,
        responses={200: ProductoSerializers, 400: "Bad Request", 404: "Not Found"},
        operation_description="Recibe los datos de un producto, calcula el precio total y devuelve el producto con el precio total."
    )
    def post(self, request):
        # Recibimos los datos del producto
        precio_unitario = request.data.get('precio_unitario')
        cantidad = request.data.get('cantidad')

        # Verificamos si los datos de precio_unitario y cantidad están presentes
        if not precio_unitario or not cantidad:
            return Response({"error": "Faltan los datos de precio_unitario o cantidad."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Convertimos el precio_unitario a Decimal para precisión
            precio_unitario = Decimal(precio_unitario)
            cantidad = int(cantidad)

            # Calculamos el precio total
            precio_total = precio_unitario * cantidad

        except Exception as e:
            return Response({"error": f"Error al calcular el precio total: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        # Creamos un diccionario con los datos del producto y el precio total calculado
        response_data = {
            "precio_unitario": str(precio_unitario),  # Aseguramos que el precio esté en formato string para evitar problemas con JSON
            "cantidad": cantidad,
            "precio_total": str(precio_total),  # Convertimos el resultado a string
        }

        return Response(response_data, status=status.HTTP_200_OK)

