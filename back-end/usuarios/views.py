from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from django.utils.timezone import now
from .serializers import TokenSerializer, UsuarioSerializer, UsuarioTokenSerializer
from .serializers import PermissionSerializer
from rest_framework import status, views
from django.contrib.auth.models import User, Permission, Group
from .serializers import UserPermissionSerializer


class UsuarioLoginView(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user.last_login = now()
        user.save()
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UsuarioTokenSerializer(user)
        return Response({
            'user': user_serializer.data,
            'token': TokenSerializer(token).data,
        }, status=status.HTTP_200_OK)

class UsuarioTokenListAPIView(generics.ListAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    permission_classes = [IsAuthenticated]

class UsuarioLogoutView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({"detail": "Logout realizado com sucesso."}, status=status.HTTP_204_NO_CONTENT)
  
class UsuarioListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUser]

class UsuarioCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUser] 

class UsuarioRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUser]

class PermissionPagination(PageNumberPagination):
    page_size = 100
class PermissionListAPIView(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    pagination_class = PermissionPagination
    permission_classes = [IsAdminUser]

class UsuarioPermissionUpdateAPIView(views.APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        permission_ids = request.data.get("permissions", [])
        for perm_id in permission_ids:
            permission = Permission.objects.get(id=perm_id)
            user.user_permissions.add(permission)
        user.save()
        return Response(UserPermissionSerializer(user).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        permission_ids = request.data.get("permissions", [])
        for perm_id in permission_ids:
            permission = Permission.objects.get(id=perm_id)
            user.user_permissions.remove(permission)
        user.save()
        return Response(UserPermissionSerializer(user).data, status=status.HTTP_200_OK)
    
class UsuarioGroupUpdateAPIView(views.APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        group_ids = request.data.get("groups", [])
        for group_id in group_ids:
            group = Group.objects.get(id=group_id)
            user.groups.add(group)
        user.save()
        return Response({"detail": "Usuário adicionado aos grupos."}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        group_ids = request.data.get("groups", [])
        for group_id in group_ids:
            group = Group.objects.get(id=group_id)
            user.groups.remove(group)
        user.save()
        return Response({"detail": "Usuário removido dos grupos."}, status=status.HTTP_200_OK)
    
class UsuarioPermissionsAPIView(views.APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        direct_permissions = user.user_permissions.all()
        group_permissions = Permission.objects.filter(group__user=user)
        all_permissions = direct_permissions | group_permissions
        serializer = PermissionSerializer(all_permissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)