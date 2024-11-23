from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer  # Corrección del nombre
from drf_yasg.utils import swagger_auto_schema

class UserCreateView(APIView):  # Corrección del nombre de la clase base
    @swagger_auto_schema(request_body=UserCreateSerializer)
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)  # Corrección del nombre

        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Usuario creado exitosamente"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Corrección del status

