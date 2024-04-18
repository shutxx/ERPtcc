from rest_framework import generics
from .models import Venda, ItensVenda
from .serializers import VendaSerializer
from rest_framework.pagination import PageNumberPagination

class VendaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    pagination_class = PageNumberPagination
