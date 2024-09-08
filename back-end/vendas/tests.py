from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Venda, ItensVenda, Cliente, Produto

class Cores:
    RESET = "\033[0m"
    VERMELHO = "\033[31m"
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    AZUL = "\033[34m"
    MAGENTA = "\033[35m"
    CIANO = "\033[36m"
    BRANCO = "\033[37m"

class VendaAPITestCase(APITestCase):

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
        self.cliente = Cliente.objects.create(
            NomePessoa="João Silva",
            CPFouCNPJ="123.456.789-00",
            NomeRua="Rua das Flores",
            Numero="123",
            NomeBairro="Centro",
            Email="joao.silva@example.com",
            Telefone="(11)98765-4321"
        )
        self.venda = Venda.objects.create(
            IdCliente=self.cliente,
            DataVenda="2024-08-22",
            TotalVenda=13599.78,
            FormaPagamento="Avista",
            Prazo="10,20",
            Parcelas=2,
        )
        self.itens_venda_data = [
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
        for item_data in self.itens_venda_data:
            ItensVenda.objects.create(IdVenda=self.venda, **item_data)

        self.url_list = reverse('vendas-list')
        self.url_create = reverse('venda-create')
        self.url_detail = reverse('venda-detail', args=[self.venda.IdVenda])
        self.url_update = reverse('venda-update', args=[self.venda.IdVenda])
        self.url_delete = reverse('venda-delete', args=[self.venda.IdVenda])


        self.MsgTest = ' '

    def test_get_venda_list(self):
        self.MsgTest = 'Teste do endpoint GET /vendas/'
        print(self.MsgTest)
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        itens_venda = response.data['results'][0]['itens_venda']
        TotalVenda = response.data['results'][0]['TotalVenda']
        self.assertGreaterEqual(len(itens_venda), 2)
        self.assertGreaterEqual(len(response.data), 1)
        print(f".{Cores.VERDE}Teste do endpoint GET /vendas/ concluído com sucesso.{Cores.RESET}")

    def test_get_venda_detail(self):
        self.MsgTest = 'Teste do endpoint GET /venda-detail/<int:pk>'
        print(self.MsgTest)
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['TotalVenda'], 13599.78)
        self.assertGreaterEqual(len(response.data['itens_venda']), 2)
        print(f".{Cores.VERDE}Teste do endpoint GET /venda-detail/<int:pk> concluído com sucesso.{Cores.RESET}")

    def test_post_venda(self):
        self.MsgTest = 'Teste do endpoint POST /venda-create/'
        print(self.MsgTest)
        data = {
            "IdCliente": 1,
            "DataVenda": "2024-08-22",
            "TotalVenda": 13599.78,
            "FormaPagamento": "Avista",
            "Prazo": "10,20",
            "Parcelas": 2,
            "itens_venda": [
                {
                    "IdProduto": 1,
                    "QtdProduto": 1,
                    "NomeProduto": "Câmera Sony Alpha a6400",
                    "ValorUnitario": 2599.99,
                    "ValorTotal": 5199.98
                },
                {
                    "IdProduto": 2,
                    "QtdProduto": 1,
                    "NomeProduto": "Smartphone Samsung Galaxy S23",
                    "ValorUnitario": 4199.9,
                    "ValorTotal": 8399.8
                }
            ]
        }
        response = self.client.post(self.url_create, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Venda.objects.count(), 2)
        self.assertGreaterEqual(len(response.data['itens_venda']), 2)
        print(f".{Cores.VERDE}Teste do endpoint POST /venda-create/ concluído com sucesso.{Cores.RESET}")
        
    def test_put_venda(self):
        self.MsgTest = 'Teste do endpoint PUT /venda-update/<int:pk>'
        print(self.MsgTest)
        data = {
            "IdCliente": 1,
            "DataVenda": "2024-08-22",
            "TotalVenda": 13599.78,
            "FormaPagamento": "A Prazo",
            "Prazo": "10,20,30,40,50",
            "Parcelas": 5,
            "itens_venda": [
                {
                    "IdProduto": 1,
                    "QtdProduto": 1,
                    "NomeProduto": "Câmera Sony Alpha a6400",
                    "ValorUnitario": 2599.99,
                    "ValorTotal": 5199.98
                },
                {
                    "IdProduto": 2,
                    "QtdProduto": 1,
                    "NomeProduto": "Smartphone Samsung Galaxy S23",
                    "ValorUnitario": 4199.9,
                    "ValorTotal": 8399.8
                }
            ]
        }
        response = self.client.put(self.url_update, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.venda.refresh_from_db()
        self.assertEqual(self.venda.IdVenda, 1)
        self.assertEqual(self.venda.FormaPagamento, 'A Prazo')
        self.assertEqual(self.venda.Prazo, '10,20,30,40,50')
        self.assertEqual(self.venda.Parcelas, 5)
        print(f".{Cores.VERDE}Teste do endpoint PUT /venda-update/ concluído com sucesso.{Cores.RESET}")
        
    def test_delete_venda(self):
        self.MsgTest = 'Teste do endpoint DELETE /compra-delete/<int:pk>'
        print(self.MsgTest)
        response = self.client.delete(self.url_delete)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Venda.objects.count(), 0)
        print(F".{Cores.VERDE}Teste do endpoint DELETE /venda-delete/<int:pk> concluído com sucesso.{Cores.RESET}")