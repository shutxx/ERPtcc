from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import TokenSerializer, UsuarioSerializer


class UsuarioLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'user': user.username, 'token': token.key})
        
class UsuarioListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioTokenListAPIView(generics.ListAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class UsuarioLogoutView(generics.DestroyAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer