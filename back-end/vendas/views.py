from rest_framework import generics
from .models import Venda
from .serializers import VendaSerializer
from rest_framework.pagination import PageNumberPagination

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