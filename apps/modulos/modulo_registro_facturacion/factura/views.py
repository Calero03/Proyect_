from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.exceptions import NotFound


from .models import Factura
from .serializers import FacturaSerializers


class FacturaApiView(APIView):

    @swagger_auto_schema(
        responses={200: FacturaSerializers(many=True)},
        operation_description="Obtiene una lista de todas las facturas."
    )
    def get(self, request):
        serializers = FacturaSerializers(Factura.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializers.data)
    
    def get_object(self, pk):
        try:
            return Factura.objects.get(pk=pk)
        except Factura.DoesNotExist:
            raise NotFound(detail="Factura no encontrada.")
    
    @swagger_auto_schema(
        request_body=FacturaSerializers,
        responses={201: FacturaSerializers, 400: "Bad Request"},
        operation_description="Crea una nueva factura."
    )
    def post(self, request):
        serializers = FacturaSerializers(data=request.data)
        try:
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(status=status.HTTP_201_CREATED, data=serializers.data)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(
        request_body=FacturaSerializers,
        responses={200: FacturaSerializers, 400: "Bad Request", 404: "Not Found"},
        operation_description="Actualiza una factura existente."
    )
    def put(self, request, pk=None):
        factura = self.get_object(pk)
        serializers = FacturaSerializers(factura, data=request.data, partial=True)
        try:
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(status=status.HTTP_200_OK, data=serializers.data)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'pk', openapi.IN_PATH, description="ID de la factura a anular",
                type=openapi.TYPE_INTEGER
            )
        ],
        responses={200: "Factura anulada exitosamente.", 404: "Not Found"},
        operation_description="Anula una factura en lugar de eliminarla, usando su ID."
    )
    def delete(self, request, pk=None):
        factura = self.get_object(pk)
        factura.estado_factura = "False" 
        factura.save()
        return Response({"detail": "Factura anulada exitosamente."}, status=status.HTTP_200_OK)
    



#BUSCAR POR RAMGO DE FECHAS, CLIENTE O ESTADO
class BusquedaAvanzadaFacturasApiView(APIView):

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('cliente_id', openapi.IN_QUERY, description="ID del cliente", type=openapi.TYPE_INTEGER),
            openapi.Parameter('estado', openapi.IN_QUERY, description="Estado de la factura", type=openapi.TYPE_STRING),
            openapi.Parameter('fecha_inicio', openapi.IN_QUERY, description="Fecha de inicio (YYYY-MM-DD)", type=openapi.TYPE_STRING),
            openapi.Parameter('fecha_fin', openapi.IN_QUERY, description="Fecha de fin (YYYY-MM-DD)", type=openapi.TYPE_STRING),
        ],
        responses={
            200: openapi.Response(
                description="Listado de facturas que cumplen los criterios de búsqueda.",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "id_factura": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID de la factura"),
                            "id_cliente__nombre": openapi.Schema(type=openapi.TYPE_STRING, description="Nombre del cliente"),
                            "estado_factura": openapi.Schema(type=openapi.TYPE_STRING, description="Estado de la factura"),
                            "fecha_factura": openapi.Schema(type=openapi.TYPE_STRING, description="Fecha de la factura"),
                        }
                    )
                )
            )
        },
        operation_description="Busca facturas según cliente, estado y/o rango de fechas."
    )
    def get(self, request):
        cliente_id = request.query_params.get('cliente_id')
        estado = request.query_params.get('estado')
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')

        queryset = Factura.objects.all()

        if cliente_id:
            queryset = queryset.filter(id_cliente_id=cliente_id)
        if estado:
            queryset = queryset.filter(estado_factura=estado)
        if fecha_inicio and fecha_fin:
            queryset = queryset.filter(fecha_factura__range=[fecha_inicio, fecha_fin])

        data = queryset.values('id_factura', 'id_cliente__nombre', 'estado_factura', 'fecha_factura')
        return Response(status=status.HTTP_200_OK, data=list(data))



#LISTADO DE FACTURAS ANULADAS
class FacturasAnuladasApiView(APIView):
    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="Listado de facturas anuladas.",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "id_factura": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID de la factura"),
                            "cliente": openapi.Schema(type=openapi.TYPE_STRING, description="Nombre del cliente"),
                            "estado_factura": openapi.Schema(type=openapi.TYPE_STRING, description="Fecha de la factura"),
                        }
                    )
                )
            )
        },
        operation_description="Obtiene un listado de todas las facturas que han sido anuladas."
    )
    def get(self, request):
        # Filtra las facturas donde estado_factura es False (anulada)
        data = Factura.objects.filter(estado_factura=False).values('id_factura', 'cliente__nombre', 'fecha_factura')
        return Response(status=status.HTTP_200_OK, data=list(data))
