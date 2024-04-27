from rest_framework import generics
from .models import ContaPagar, ContaReceber
from .serializers import ContaPagarSerializer, ContaReceberSerializer
from rest_framework.pagination import PageNumberPagination

class ContasPagar():
    class ContaPagarListAPIView(generics.ListAPIView):
        queryset =  ContaPagar.objects.all()
        serializer_class = ContaPagarSerializer
        pagination_class = PageNumberPagination

    class ContaPagarCreateAPIView(generics.CreateAPIView):
        queryset =  ContaPagar.objects.all()
        serializer_class = ContaPagarSerializer

    class ContaPagarRetrieveAPIView(generics.RetrieveAPIView):
        queryset =  ContaPagar.objects.all()
        serializer_class = ContaPagarSerializer 

    class ContaPagarUpdateAPIView(generics.UpdateAPIView):
        queryset =  ContaPagar.objects.all()
        serializer_class = ContaPagarSerializer

    class ContaPagarDestroyAPIView(generics.DestroyAPIView):
        queryset =  ContaPagar.objects.all()
        serializer_class = ContaPagarSerializer 

class ContasReceber():
    class ContaReceberListAPIView(generics.ListAPIView):
        queryset =  ContaReceber.objects.all()
        serializer_class = ContaReceberSerializer
        pagination_class = PageNumberPagination

    class ContaReceberCreateAPIView(generics.CreateAPIView):
        queryset =  ContaReceber.objects.all()
        serializer_class = ContaReceberSerializer

    class ContaReceberRetrieveAPIView(generics.RetrieveAPIView):
        queryset =  ContaReceber.objects.all()
        serializer_class = ContaReceberSerializer 

    class ContaReceberUpdateAPIView(generics.UpdateAPIView):
        queryset =  ContaReceber.objects.all()
        serializer_class = ContaReceberSerializer

    class ContaReceberDestroyAPIView(generics.DestroyAPIView):
        queryset =  ContaReceber.objects.all()
        serializer_class = ContaReceberSerializer 