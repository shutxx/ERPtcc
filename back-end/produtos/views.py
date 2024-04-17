from rest_framework import generics
from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework.pagination import PageNumberPagination

class ProdutoListAPIView(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    pagination_class = PageNumberPagination

class ProdutoCreateAPIView(generics.CreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoDestroyAPIView(generics.DestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoUpdateAPIView(generics.UpdateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer