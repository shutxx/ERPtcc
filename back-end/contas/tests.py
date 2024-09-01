from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ContaPagar, ContaReceber
from compras.models import Compra, ItensCompra, Fornecedor, Produto

class Cores:
    RESET = "\033[0m"
    VERMELHO = "\033[31m"
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    AZUL = "\033[34m"
    MAGENTA = "\033[35m"
    CIANO = "\033[36m"
    BRANCO = "\033[37m"

class ContaPagarAPITestCase(APITestCase):

    def setUp(self):
        self.produto1 = Produto.objects.create(
            NomeProduto="Câmera GoPro HERO9",
            Descricao=("Câmera de ação à prova d'água com resolução 5K, "
                       "gravação em 60fps, "
                       "estabilização HyperSmooth 3.0, "
                       "até 30 metros de profundidade."),
            Preco=2599.99,
            UnidMedida="Unidade",
            Estoque=40
        )
        self.produto2 = Produto.objects.create(
            NomeProduto="Smartphone Samsung Galaxy S21",
            Descricao=("Smartphone com tela AMOLED de 6.2 polegadas, "
                       "processador Exynos 2100, 8GB de RAM, "
                       "128GB de armazenamento, "
                       "câmera tripla de 64MP."),
            Preco=4199.90,
            UnidMedida="Unidade",
            Estoque=30
        )
        self.fornecedor = Fornecedor.objects.create(
            NomeFantasia="Techno Sound",
            NomeJuridico="Techno Sound Equipamentos Eletrônicos Ltda.",
            Email="suporte@technosound.com.br",
            Telefone="(11)90123-4567",
            CNPJ="50.137.240/0001-00",
            NomeRua="Avenida do Som",
            Numero="950",
            NomeBairro="Eletrônico"
        )
        self.compra = Compra.objects.create(
            IdFornecedor=self.fornecedor,
            DataCompra="2024-08-22",
            ValorTotal=123199.78,
            FormaPagamento="A Prazo",
            Prazo="10,20,30,40",
            Parcelas=4,
        )
        self.itens_compra_data = [
            {
                "IdProduto": self.produto1,
                "NomeProduto": "Câmera GoPro HERO9",
                "ValorUnitario": 2599.99,
                "QtdProduto": 22,
                "ValorTotal": 57199.78
            },
            {
                "IdProduto": self.produto2,
                "NomeProduto": "Smartphone Samsung Galaxy S21",
                "ValorUnitario": 4199.9,
                "QtdProduto": 22,
                "ValorTotal": 66000.00
            }
        ]
        for item_data in self.itens_compra_data:
            ItensCompra.objects.create(IdCompra=self.compra, **item_data)

        self.contaPagar = ContaPagar.objects.create(
                IdCompra=self.compra,
                Valor=1500.00,
                DataVencimento="2024-04-17",
                DataEntrada="2024-04-17",
                Status="True"
        )

        self.url_list = reverse('conta-pagar-list')
        self.url_create = reverse('conta-create')
        self.url_detail = reverse('conta-detail', args=[self.contaPagar.IdContaPagar])
        self.url_update = reverse('conta-update', args=[self.contaPagar.IdContaPagar])
        self.url_delete = reverse('conta-delete', args=[self.contaPagar.IdContaPagar])

    def test_get_conta_pagar_list(self):
        """Testar o endpoint GET /contas-pagar/"""
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        print(f"{Cores.VERDE}Teste para endpoint GET /contas-pagar/ concluído com sucesso.{Cores.RESET}")