from rest_framework import generics
from rest_framework.views import APIView
from django.db.models import Q
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

class ProdutoSearch(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', None)

        if query:
            produtoSeach = Produto.objects.filter(
                Q(NomeProduto__icontains=query) | Q(Descricao__icontains=query)
            )
        else:
            produtoSeach = Produto.objects.all()

        pagination_class = PageNumberPagination()
        pagination_class.page_size = 10

        result_page = pagination_class.paginate_queryset(produtoSeach, request)

        serializer_class = ProdutoSerializer(result_page, many=True)

        return pagination_class.get_paginated_response(serializer_class.data)