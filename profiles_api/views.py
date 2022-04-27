from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Testando APIViews """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None ):
        """Retorna uma lista de APIViews features"""

        lista_de_coisas = [
            'use os metodos Https nas funçoes (get, post, patch, put, delete)',
            'é similar ao tradicinal django view',
            'da a voce maior controle a logica da aplicação',
            'as urls sao mapeadas manualmentes',
        ]

        return Response({'message': 'Hello!', 'lista_de_coisa': lista_de_coisas})

    def post(self, request):
        """Criando um Hello com nosso nome"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """manipulando atualização de objeto"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Manipulando uma atualização parcial"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Apaga um objeto"""
        return Response({'method': 'DELETE'})

