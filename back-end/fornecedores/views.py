from rest_framework import generics
from rest_framework.views import APIView
from django.db.models import Q
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

class FornecedorSearch(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', None)
        if query:
            fornecedorSeach = Fornecedor.objects.filter(
                Q(NomeFantasia__icontains=query) | Q(CNPJ__icontains=query)
            )
        else:
            fornecedorSeach = Fornecedor.objects.all()
        pagination_class = PageNumberPagination()
        pagination_class.page_size = 10
        result_page = pagination_class.paginate_queryset(fornecedorSeach, request)
        serializer_class = FornecedorSerializer(result_page, many=True)
        return pagination_class.get_paginated_response(serializer_class.data)