from rest_framework import generics
from .models import Fornecedor
from .serializers import FornecedorSerializer
from rest_framework.pagination import PageNumberPagination

class FornecedorListAPIView(generics.ListAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
    pagination_class = PageNumberPagination

class FornecedorCreateAPIView(generics.CreateAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class FornecedorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class =FornecedorSerializer

class FornecedorDestroyAPIView(generics.DestroyAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class FornecedorUpdateAPIView(generics.UpdateAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer