from rest_framework import generics
from .models import ContaPagar, ContaReceber
from .serializers import ContaPagarSerializer, ContaReceberSerializer
from rest_framework.pagination import PageNumberPagination

from vendas.serializers import VendaContaSerializer
from vendas.models import Venda
from compras.models import Compra
from compras.serializers import CompraContaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ContasPagar():
    class ContaPagarListAPIView(APIView):
        def get(self, request):
            compras = Compra.objects.all()
            response_data = []
            
            paginator = PageNumberPagination()

            for compra in compras:
                contas_pagar = ContaPagar.objects.filter(IdCompra=compra.IdCompra)
                contas_pagar_serializer = ContaPagarSerializer(contas_pagar, many=True)
                compra_serializer = CompraContaSerializer(compra)

                response_data.append({
                    "compra": compra_serializer.data,
                    "parcelas": contas_pagar_serializer.data
                })

            paginated_response_data = paginator.paginate_queryset(response_data, request)
            return paginator.get_paginated_response(paginated_response_data)
        
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
    class ContaReceberListAPIView(APIView):
        def get(self, request):
            vendas = Venda.objects.all()
            response_data = []
            
            paginator = PageNumberPagination()

            for venda in vendas:
                contas_receber = ContaReceber.objects.filter(IdVenda=venda.IdVenda)
                contas_receber_serializer = ContaReceberSerializer(contas_receber, many=True)
                venda_serializer = VendaContaSerializer(venda)

                response_data.append({
                    "venda": venda_serializer.data,
                    "parcelas": contas_receber_serializer.data
                })

            paginated_response_data = paginator.paginate_queryset(response_data, request)
            return paginator.get_paginated_response(paginated_response_data)

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