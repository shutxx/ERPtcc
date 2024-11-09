from rest_framework.views import APIView
from compras.models import Compra
from vendas.models import Venda
from clientes.models import Cliente
from fornecedores.models import Fornecedor
from produtos.models import Produto
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import render_to_string

class RelatorioCompraView(APIView):
    def get(self, request, *args, **kwargs):
        compras = Compra.objects.all()
        html_content = render_to_string('relatorio_compra.html', {'compras': compras})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_compra.pdf"'
        pisa.CreatePDF(html_content, dest=response)
        return response
    
class RelatorioVendaView(APIView):
    def get(self, request, *args, **kwargs):
        vendas = Venda.objects.all()
        html_content = render_to_string('relatorio_venda.html', {'vendas': vendas})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_venda.pdf"'
        pisa.CreatePDF(html_content, dest=response)
        return response
    
class RelatorioClienteView(APIView):
    def get(self, request, *args, **kwargs):
        clientes = Cliente.objects.all()
        html_content = render_to_string('relatorio_clientes.html', {'clientes': clientes})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_clientes.pdf"'
        pisa.CreatePDF(html_content, dest=response)
        return response
    
class RelatorioFornecedorView(APIView):
    def get(self, request, *args, **kwargs):
        fornecedores = Fornecedor.objects.all()
        html_content = render_to_string('relatorio_fornecedores.html', {'fornecedores': fornecedores})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_fornecedores.pdf"'
        pisa.CreatePDF(html_content, dest=response)
        return response
    
class RelatorioProdutoView(APIView):
    def get(self, request, *args, **kwargs):
        produtos = Produto.objects.all()
        html_content = render_to_string('relatorio_produtos.html', {'produtos': produtos})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_produtos.pdf"'
        pisa.CreatePDF(html_content, dest=response)
        return response