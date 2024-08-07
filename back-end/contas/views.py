from rest_framework import generics
from .models import ContaPagar, ContaReceber
from .serializers import ContaPagarSerializer, ContaReceberSerializer
from rest_framework.pagination import PageNumberPagination

from vendas.serializers import VendaContaSerializer
from vendas.models import Venda
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
    # class ContaReceberListAPIView(generics.ListAPIView):
    #     queryset =  ContaReceber.objects.all()
    #     serializer_class = ContaReceberSerializer
    #     pagination_class = PageNumberPagination

    class ContaReceberListAPIView(APIView):
        def get(self, request):
            vendas = Venda.objects.all()
            response_data = []

            paginator = PageNumberPagination()

            for venda in vendas:
                contas_receber = ContaReceber.objects.filter(IdVenda=venda)
                paginated_contas_receber = paginator.paginate_queryset(contas_receber, request)
                contas_receber_serializer = ContaReceberSerializer(paginated_contas_receber, many=True)
                venda_serializer = VendaContaSerializer(venda)

                response_data.append({
                    "venda": venda_serializer.data,
                    "parcelas": contas_receber_serializer.data
                })

            return paginator.get_paginated_response(response_data)


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