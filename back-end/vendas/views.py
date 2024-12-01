from rest_framework import generics
from .models import Venda, ItensVenda 
from .serializers import VendaSerializer, VendaContaSerializer
from django.db.models import Q
from datetime import datetime
from contas.serializers import ContaReceberSerializer
from contas.models import EstornoLog
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


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

        if not query:
            return Response({"error": "O parâmetro 'query' é obrigatório."}, status=400)
        
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
    

class VendaEstornoView(APIView):
    def post(self, request, *args, **kwargs):
        venda_id = request.query_params.get('venda_id')
        motivo = request.data.get('motivo')

        if not venda_id:
            return Response({"error": "O parâmetro 'venda_id' é obrigatório."}, status=400)

        venda = Venda.objects.prefetch_related('contareceber_set').get(IdVenda=int(venda_id))

        contas_receber = venda.contareceber_set.all()
        for conta in contas_receber:
            conta.Estornada = True
            conta.save()

        venda.Estornada = True
        venda.save()

        itens_venda = ItensVenda.objects.all()
        itens_venda = itens_venda.filter(IdVenda=venda_id)
        for item in itens_venda:
            produto = item.IdProduto
            produto.adicionar_quantidade(item.QtdProduto)
            produto.save()


        EstornoLog.objects.create(
            IdVenda=venda,
            DataEstorno=datetime.now(),
            Motivo=motivo
        )

        return Response({'resposta': 'venda estornada'}, status=200)