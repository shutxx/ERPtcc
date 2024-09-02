from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Compra, ItensCompra, Fornecedor, Produto

class Cores:
    RESET = "\033[0m"
    VERMELHO = "\033[31m"
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    AZUL = "\033[34m"
    MAGENTA = "\033[35m"
    CIANO = "\033[36m"
    BRANCO = "\033[37m"

class CompraAPITestCase(APITestCase):

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
            

        self.url_list = reverse('compras-list')
        self.url_create = reverse('compra-create')
        self.url_detail = reverse('compra-detail', args=[self.compra.IdCompra])
        self.url_update = reverse('compra-update', args=[self.compra.IdCompra])
        self.url_delete = reverse('compra-delete', args=[self.compra.IdCompra])

        self.MsgTest = ' '
        
    def test_get_compras_list(self):
        self.MsgTest = 'Teste do endpoint GET /compras/'
        print(self.MsgTest)
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        print(f".{Cores.VERDE}Teste do endpoint GET /compras/ concluído com sucesso.{Cores.RESET}")

    def test_get_compra_detail(self):
        self.MsgTest = 'Teste do endpoint GET /compra/detail/<int:pk>'
        print(self.MsgTest)
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ValorTotal'], 123199.78)
        self.assertGreaterEqual(len(response.data['itens_compra']), 2)
        print(f".{Cores.VERDE}Teste do endpoint GET /compra/detail/<int:pk> concluído com sucesso.{Cores.RESET}")

    def test_post_compras(self):
        self.MsgTest = 'Teste do endpoint POST /compra/create/'
        print(self.MsgTest)
        data = {
            "IdFornecedor": 1,
            "DataCompra": "2024-08-22",
            "ValorTotal": 123199.78,
            "FormaPagamento": "A Prazo",
            "Prazo": "10,20,30,40",
            "Parcelas": 4,
            "itens_compra": [
                {
                    "IdProduto": 1,
                    "NomeProduto": "Câmera GoPro HERO9",
                    "ValorUnitario": 2599.99,
                    "QtdProduto": 22,
                    "ValorTotal": 57199.78
                },
                {
                    "IdProduto": 2,
                    "NomeProduto": "Smartphone Samsung Galaxy S21",
                    "ValorUnitario": 4199.9,
                    "QtdProduto": 22,
                    "ValorTotal": 66000.00
                }
            ]
        }
        response = self.client.post(self.url_create, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Compra.objects.count(), 2)
        self.assertGreaterEqual(len(response.data['itens_compra']), 2)
        print(f".{Cores.VERDE}Teste do endpoint POST /compra/create/ concluído com sucesso.{Cores.RESET}")
        
    def test_put_compras(self):
        self.MsgTest = 'Teste do endpoint PUT /compra/update/<int:pk>'
        print(self.MsgTest)
        data = {
            "IdFornecedor": 1,
            "DataCompra": "2024-08-22",
            "ValorTotal": 123199.78,
            "FormaPagamento": "Avista",
            "Prazo": "10,20,30",
            "Parcelas": 3,
            "itens_compra": [
                {
                    "IdProduto": 1,
                    "NomeProduto": "Câmera GoPro HERO9",
                    "ValorUnitario": 2599.99,
                    "QtdProduto": 22,
                    "ValorTotal": 57199.78
                },
                {
                    "IdProduto": 2,
                    "NomeProduto": "Smartphone Samsung Galaxy S21",
                    "ValorUnitario": 4199.9,
                    "QtdProduto": 22,
                    "ValorTotal": 66000.00
                }
            ]
        }
        response = self.client.put(self.url_update, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.compra.refresh_from_db()
        self.assertEqual(self.compra.FormaPagamento, "Avista")
        self.assertEqual(self.compra.Prazo, "10,20,30")
        self.assertEqual(self.compra.Parcelas, 3)
        print(f".{Cores.VERDE}Teste do endpoint PUT /compra/update/ concluído com sucesso.{Cores.RESET}")
        
    def test_delete_compra(self):
        self.MsgTest = 'Teste do endpoint DELETE /compra/delete/<int:pk>'
        print(self.MsgTest)
        """Testa o endpoint DELETE /compra/delete/<int:pk>"""
        response = self.client.delete(self.url_delete)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Compra.objects.count(), 0)
        print(F".{Cores.VERDE}Teste do endpoint DELETE /compra/delete/<int:pk> concluído com sucesso.{Cores.RESET}")