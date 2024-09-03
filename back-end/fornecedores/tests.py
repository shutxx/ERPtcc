from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Fornecedor

class Cores:
    RESET = "\033[0m"
    VERMELHO = "\033[31m"
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    AZUL = "\033[34m"
    MAGENTA = "\033[35m"
    CIANO = "\033[36m"
    BRANCO = "\033[37m"

class FornecedorAPITestCase(APITestCase):

    def setUp(self):
        self.fornecedor = Fornecedor.objects.create(
            NomeFantasia="Techno Sound", 
            NomeJuridico="Techno Sound Equipamentos Eletrônicos Ltda.", 
            CNPJ="51.543.090/0001-06", 
            NomeRua="Avenida do Som", 
            Numero="950", 
            NomeBairro="Eletrônico", 
            Email="suporte@technosound.com.br",
            Telefone="(11)90123-4567"
        )
        self.url_list = reverse('fornecedores-list')
        self.url_create = reverse('fornecedor-create')
        self.url_detail = reverse('fornecedor-detail', args=[self.fornecedor.IdFornecedor])
        self.url_delete = reverse('fornecedor-delete', args=[self.fornecedor.IdFornecedor])
        self.url_update = reverse('fornecedor-update', args=[self.fornecedor.IdFornecedor])

        self.MsgTest = ''

    def test_get_fornecedor_list(self):
        self.MsgTest = 'Teste do endpoint GET /fornecedores-list/'
        print(self.MsgTest)
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        print(f".{Cores.VERDE}Teste do endpoint GET /fornecedores-list/ concluído com sucesso.{Cores.RESET}")

    def test_get_fornecedor_detail(self):
        self.MsgTest = 'Teste do endpoint GET /fornecedor-detail/<int:pk>'
        print(self.MsgTest)
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['NomeFantasia'], "Techno Sound")
        print(f".{Cores.VERDE}Teste do endpoint GET /fornecedor-detail/<int:pk> concluído com sucesso.{Cores.RESET}")

    def test_post_fornecedor(self):
        self.MsgTest = 'Teste do endpoint POST /fornecedor-create/'
        print(self.MsgTest)
        data = {
            "NomeFantasia": "Techno Sound",
            "NomeJuridico": "Techno Sound Equipamentos Eletrônicos Ltda.",
            "Email": "suporte@technosound.com.br",
            "Telefone": "(11)90123-4567",
            "CNPJ": "90.124.304/0001-53",
            "NomeRua": "Avenida do Som",
            "Numero": "950",
            "NomeBairro": "Eletrônico"
        }
        response = self.client.post(self.url_create, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Fornecedor.objects.count(), 2)
        print(f".{Cores.VERDE}Teste do endpoint POST /fornecedor-create/ concluído com sucesso.{Cores.RESET}")

    def test_update_fornecedor(self):
        self.MsgTest = 'Teste do endpoint PUT /fornecedor-update/<int:pk>'
        print(self.MsgTest)
        data = {
            "NomeFantasia": "Techno Sound",
            "NomeJuridico": "Techno Sound Equipamentos",
            "Email": "suporte@technosound.com.br",
            "Telefone": "(11)90123-4567",
            "CNPJ": "90.124.304/0001-53",
            "NomeRua": "Avenida do Som",
            "Numero": "1950",
            "NomeBairro": "Pq industrial"
        }
        response = self.client.put(self.url_update, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.fornecedor.refresh_from_db()
        self.assertEqual(self.fornecedor.NomeJuridico, 'Techno Sound Equipamentos')
        print(f".{Cores.VERDE}Teste do endpoint PUT /fornecedor-update/<int:pk> concluído com sucesso.{Cores.RESET}")

    def test_delete_fornecedor(self):
        self.MsgTest = 'Teste do endpoint DELETE /fornecedor-delete/<int:pk>'
        print(self.MsgTest)
        response = self.client.delete(self.url_delete)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Fornecedor.objects.count(), 0)
        print(F".{Cores.VERDE}Teste do endpoint DELETE /fornecedor-delete/<int:pk> concluído com sucesso.{Cores.RESET}")