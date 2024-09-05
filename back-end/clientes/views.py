from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.pagination import PageNumberPagination
# from rest_framework import permissions

class ClienteListCreateAPIView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    pagination_class = PageNumberPagination

class ClienteCreateAPIView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ClienteRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ClienteDestroyAPIView(generics.DestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ClienteUpdateAPIView(generics.UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # permission_classes = [permissions.IsAuthenticated]