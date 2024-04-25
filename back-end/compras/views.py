from rest_framework import generics
from .models import Compra
from .serializers import CompraSerializer
from rest_framework.pagination import PageNumberPagination

class CompraListCreateAPIView(generics.ListCreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    pagination_class = PageNumberPagination