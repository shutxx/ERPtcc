from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Produto

class Cores:
    RESET = "\033[0m"
    VERMELHO = "\033[31m"
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    AZUL = "\033[34m"
    MAGENTA = "\033[35m"
    CIANO = "\033[36m"
    BRANCO = "\033[37m"

class ProdutoAPITestCase(APITestCase):

    def setUp(self):
        self.produto = Produto.objects.create(
            NomeProduto="Câmera Sony Alpha a6400",
            Descricao="Câmera mirrorless com sensor APS-C, gravação em 4K, foco automático rápido, e tela LCD articulada.",
            Preco=6499.00,
            UnidMedida="Unidade",
            Estoque=22
        )

        self.url_list = reverse('produtos-list')
        self.url_create = reverse('produto-create')
        self.url_detail = reverse('produto-detail', args=[self.produto.IdProduto])
        self.url_delete = reverse('produto-delete', args=[self.produto.IdProduto])
        self.url_update = reverse('produto-update', args=[self.produto.IdProduto])

        self.MsgTest = ''

    def test_get_produto_list(self):
        self.MsgTest = 'Teste do endpoint GET /produtos-list/'
        print(self.MsgTest)
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)
        print(f".{Cores.VERDE}Teste do endpoint GET /produtos-list/ concluído com sucesso.{Cores.RESET}")

    def test_get_produto_detail(self):
        self.MsgTest = 'Teste do endpoint GET /produto-detail/<int:pk>'
        print(self.MsgTest)
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['NomeProduto'], "Câmera Sony Alpha a6400")
        print(f".{Cores.VERDE}Teste do endpoint GET /produto-detail/<int:pk> concluído com sucesso.{Cores.RESET}")

    def test_post_produto(self):
        self.MsgTest = 'Teste do endpoint POST /produto-create/'
        print(self.MsgTest)
        data = {
            "NomeProduto": "Roteador TP-Link Archer AX73",
            "Descricao": "Roteador Wi-Fi 6 com velocidades de até 5400 Mbps, quatro antenas externas, e cobertura de longo alcance.",
            "Preco": 599.00,
            "UnidMedida": "Unidade",
            "Estoque": 18
        }
        response = self.client.post(self.url_create, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produto.objects.count(), 2)
        print(f".{Cores.VERDE}Teste do endpoint POST /produto-create/ concluído com sucesso.{Cores.RESET}")

    def test_update_produto(self):
        self.MsgTest = 'Teste do endpoint PUT /produto-update/<int:pk>'
        print(self.MsgTest)
        data = {
            "NomeProduto": "Roteador",
            "Descricao": "Roteador Wi-Fi 6 com velocidades de até 5400 Mbps, quatro antenas externas, e cobertura de longo alcance.",
            "Preco": 99.00,
            "UnidMedida": "Unidade",
            "Estoque": 18
        }
        response = self.client.put(self.url_update, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.NomeProduto, "Roteador")
        self.assertEqual(self.produto.Preco, 99.00)
        print(f".{Cores.VERDE}Teste do endpoint PUT /produto-update/<int:pk> concluído com sucesso.{Cores.RESET}")

    def test_delete_produto(self):
        self.MsgTest = 'Teste do endpoint DELETE /produto-delete/<int:pk>'
        print(self.MsgTest)
        response = self.client.delete(self.url_delete)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Produto.objects.count(), 0)
        print(f".{Cores.VERDE}Teste do endpoint DELETE /produto-delete/<int:pk> concluído com sucesso.{Cores.RESET}")