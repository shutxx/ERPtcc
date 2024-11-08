from rest_framework import generics
from .models import Venda
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

class RelatorioView(APIView):
    def get(self, request, *args, **kwargs):
        vendas = Venda.objects.all()
        html_content = render_to_string('relatorio.html', {'vendas': vendas})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'
        pisa.CreatePDF(html_content, dest=response)
        return response