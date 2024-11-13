from rest_framework.views import APIView
from compras.models import Compra
from vendas.models import Venda
from clientes.models import Cliente
from fornecedores.models import Fornecedor
from produtos.models import Produto
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.dateparse import parse_date


class RelatorioCompraView(APIView):
    def get(self, request, *args, **kwargs):
        data_inicio = request.query_params.get('data_inicio')
        data_fim = request.query_params.get('data_fim')
        fornecedor = request.query_params.get('fornecedor')
        
        compras = Compra.objects.all()
        
        if data_inicio:
            compras = compras.filter(DataCompra__gte=parse_date(data_inicio))
        if data_fim:
            compras = compras.filter(DataCompra__lte=parse_date(data_fim))
        if fornecedor:
            compras = compras.filter(IdFornecedor__IdFornecedor=int(fornecedor))
        
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
        vendas = Venda.objects.all()
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