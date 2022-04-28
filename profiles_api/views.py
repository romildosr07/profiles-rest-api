from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers, models, permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Testando API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Retornando uma messagen de Hello"""
        a_viewset = [
            'Açoes que usa (list, create, retrieve, update, partial_update)',
            'Mapeamento automatico usando rotas',
            'prover mais funcionalidades com menos condigos',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Cria uma nova messagem de Hello"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Lida com obtençao de objetos por id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """lida com atualização de um objeto"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """lida com atualização de parte do objeto"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """lida com a remoção de um objeto"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """lida com criaçao e atualizaçao de perfil"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.object.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """lida com a criação de auttenticação token de usuario"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
