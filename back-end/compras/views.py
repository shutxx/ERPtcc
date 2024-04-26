from rest_framework import generics
from .models import Compra
from .serializers import CompraSerializer
from rest_framework.pagination import PageNumberPagination

class CompraListAPIView(generics.ListAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    pagination_class = PageNumberPagination

class CompraCreateAPIView(generics.CreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class CompraRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class CompraDestroyAPIView(generics.DestroyAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class CompraUpdateAPIView(generics.UpdateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer