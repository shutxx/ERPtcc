from rest_framework import generics
from rest_framework.views import APIView
from django.db.models import Q
from .models import Compra
from .serializers import CompraSerializer
from rest_framework.pagination import PageNumberPagination
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import render_to_string

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

class RelatorioView(APIView):
    def get(self, request, *args, **kwargs):
        compras = Compra.objects.all()
        html_content = render_to_string('relatorio_compra.html', {'compras': compras})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_compra.pdf"'
        pisa.CreatePDF(html_content, dest=response)
        return response

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