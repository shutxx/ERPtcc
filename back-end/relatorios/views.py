from rest_framework.views import APIView
from compras.models import Compra
from compras.serializers import CompraContaSerializer
from vendas.models import Venda
from clientes.models import Cliente
from contas.models import ContaPagar, ContaReceber
from contas.serializers import ContaPagarSerializer
from fornecedores.models import Fornecedor
from produtos.models import Produto
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.dateparse import parse_date
from django.db.models import Sum, F


class RelatorioCompraView(APIView):
    def get(self, request, *args, **kwargs):
        data_inicio = request.query_params.get('data_inicio')
        data_fim = request.query_params.get('data_fim')
        fornecedor = request.query_params.get('fornecedor')
        produto = request.query_params.get('produto')
        top_fornecedor = request.query_params.get('fornecedor')
        
        compras = Compra.objects.all()
        
        if data_inicio:
            compras = compras.filter(DataCompra__gte=parse_date(data_inicio))
        if data_fim:
            compras = compras.filter(DataCompra__lte=parse_date(data_fim))
        if fornecedor:
            compras = compras.filter(IdFornecedor=int(fornecedor))
        if produto:
            compras = compras.filter(itens_compra__IdProduto=int(produto))
        if top_fornecedor:
            compras = compras.values('IdFornecedor') \
            .annotate(total_compras=Sum(F('itens_compra__QtdProduto')* F('itens_compra__ValorUnitario'))) \
            .order_by('-total_compras')[:int(top_fornecedor)]
        
        html_content = render_to_string('relatorio_compra.html', {'compras': compras})
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_compra.pdf"'
        
        try:
            pisa_status = pisa.CreatePDF(html_content, dest=response)
            if pisa_status.err:
                return Response({'error': 'Erro ao gerar o PDF'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response

    
class RelatorioVendaView(APIView):
    def get(self, request, *args, **kwargs):
        data_inicio = request.query_params.get('data_inicio')
        data_fim = request.query_params.get('data_fim')
        cliente = request.query_params.get('cliente')
        produto = request.query_params.get('produto')
        top_cliente = request.query_params.get('top_cliente')

        vendas = Venda.objects.all()

        if data_inicio:
            vendas = vendas.filter(DataVenda__gte=parse_date(data_inicio))
        if data_fim:
            vendas = vendas.filter(DataVenda__lte=parse_date(data_fim))
        if cliente:
            vendas = vendas.filter(IdCliente=int(cliente))
        if produto:
            vendas = vendas.filter(itens_venda__IdProduto=int(produto))
        if top_cliente:
            vendas = vendas.values('IdCliente') \
                        .annotate(total_compras=Sum(F('itens_venda__QtdProduto') * F('itens_venda__ValorUnitario'))) \
                        .order_by('-total_compras')[:int(top_cliente)]
            if cliente:
                vendas = vendas.filter(IdCliente=int(cliente))
            clientes_mais_compraram = [venda['IdCliente'] for venda in vendas]
            vendas = []
            for i in clientes_mais_compraram:
                vendas.append(Venda.objects.filter(IdCliente__IdPessoa__in=clientes_mais_compraram))

            vendas = Venda.objects.filter(IdCliente__IdPessoa__in=clientes_mais_compraram)

        html_content = render_to_string('relatorio_venda.html', {'vendas': vendas})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_venda.pdf"'

        try:
            pisa_status = pisa.CreatePDF(html_content, dest=response)
            if pisa_status.err:
                return Response({'error': 'Erro ao gerar o PDF'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
    

class RelatorioClienteView(APIView):
    def get(self, request, *args, **kwargs):
        clientes = Cliente.objects.all()

        html_content = render_to_string('relatorio_clientes.html', {'clientes': clientes})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_clientes.pdf"'

        try:
            pisa_status = pisa.CreatePDF(html_content, dest=response)
            if pisa_status.err:
                return Response({'error': 'Erro ao gerar o PDF'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
    

class RelatorioFornecedorView(APIView):
    def get(self, request, *args, **kwargs):
        fornecedores = Fornecedor.objects.all()

        html_content = render_to_string('relatorio_fornecedores.html', {'fornecedores': fornecedores})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_fornecedores.pdf"'

        try:
            pisa_status = pisa.CreatePDF(html_content, dest=response)
            if pisa_status.err:
                return Response({'error': 'Erro ao gerar o PDF'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
    

class RelatorioProdutoView(APIView):
    def get(self, request, *args, **kwargs):
        produtos = Produto.objects.all()
        html_content = render_to_string('relatorio_produtos.html', {'produtos': produtos})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_produtos.pdf"'

        try:
            pisa_status = pisa.CreatePDF(html_content, dest=response)
            if pisa_status.err:
                return Response({'error': 'Erro ao gerar o PDF'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
    
class RelatorioContaAPagarView(APIView):
    def get(self, request, *args, **kwargs):
        response_data = []
        compras = Compra.objects.all()
        
        for compra in compras:
            contas_pagar = ContaPagar.objects.filter(IdCompra=compra.IdCompra)
            contas_pagar_serializer = ContaPagarSerializer(contas_pagar, many=True)
            compra_serializer = CompraContaSerializer(compra)

            response_data.append({
                "compra": compra_serializer.data,
                "parcelas": contas_pagar_serializer.data
            })
        
        html_content = render_to_string('relatorio_contas_pagar.html', {'contasAPagar': response_data})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_contas_pagar.pdf"'

        try:
            pisa_status = pisa.CreatePDF(html_content, dest=response)
            if pisa_status.err:
                return Response({'error': 'Erro ao gerar o PDF'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response