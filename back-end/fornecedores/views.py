from rest_framework import generics
from .models import Fornecedor
from .serializers import FornecedorSerializer

class FornecedorListAPIView(generics.ListAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

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