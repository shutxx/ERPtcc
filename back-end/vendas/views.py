from rest_framework import generics
from .models import Venda
from django.db.models import Q
from .serializers import VendaSerializer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import render_to_string


class VendaListAPIView(generics.ListAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    pagination_class = PageNumberPagination

class VendaCreateAPIView(generics.CreateAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class VendaRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class VendaDestroyAPIView(generics.DestroyAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class VendaUpdateAPIView(generics.UpdateAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    
class VendaSearch(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', None)
        if query:
            vendaSeach = Venda.objects.filter(
                Q(IdCliente__NomePessoa__icontains=query) | Q(IdCliente__CPFouCNPJ__icontains=query)
            )
        else:
            vendaSeach = Venda.objects.all()
        pagination_class = PageNumberPagination()
        pagination_class.page_size = 10
        result_page = pagination_class.paginate_queryset(vendaSeach, request)
        serializer_class = VendaSerializer(result_page, many=True)
        return pagination_class.get_paginated_response(serializer_class.data)