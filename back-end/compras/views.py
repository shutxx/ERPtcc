from rest_framework import generics
from rest_framework.views import APIView
from django.db.models import Q
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

class CompraSearch(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', None) 

        if query:
            compraSeach = Compra.objects.filter(
                Q(IdFornecedor__NomeFantasia__icontains=query) | Q(IdFornecedor__CNPJ__icontains=query)
            )
        else:
            compraSeach = Compra.objects.all()

        pagination_class = PageNumberPagination()
        pagination_class.page_size = 10

        result_page = pagination_class.paginate_queryset(compraSeach, request)

        serializer_class = CompraSerializer(result_page, many=True)

        return pagination_class.get_paginated_response(serializer_class.data)