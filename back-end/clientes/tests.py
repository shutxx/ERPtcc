from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Cliente

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class Cores:
    RESET = "\033[0m"
    VERMELHO = "\033[31m"
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    AZUL = "\033[34m"
    MAGENTA = "\033[35m"
    CIANO = "\033[36m"
    BRANCO = "\033[37m"

class ClienteCPFAPITestCase(APITestCase):
    
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.cliente = Cliente.objects.create(
            NomePessoa="João Silva",
            CPFouCNPJ="123.456.789-00",
            NomeRua="Rua das Flores",
            Numero="123",
            NomeBairro="Centro",
            Email="joao.silva@example.com",
            Telefone="(11)98765-4321",
            Cidade="Cianorte"
        )
        self.url_list = reverse('clientes-list')
        self.url_create = reverse('cliente-create')
        self.url_detail = reverse('cliente-detail', args=[self.cliente.IdPessoa])
        self.url_delete = reverse('cliente-delete', args=[self.cliente.IdPessoa])
        self.url_update = reverse('cliente-update', args=[self.cliente.IdPessoa])

        self.MsgTest = ''

    def test_get_clientesCPF_list(self):
        self.MsgTest = 'Teste do endpoint GET /clientes/'
        print(self.MsgTest)
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        print(f".{Cores.VERDE}Teste do endpoint GET /clientes/ concluído com sucesso.{Cores.RESET}")

    def test_get_clienteCPF_detail(self):
        self.MsgTest = 'Teste do endpoint GET /cliente-detail/<int:pk>'
        print(self.MsgTest)
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['NomePessoa'], "João Silva")
        print(f".{Cores.VERDE}Teste do endpoint GET /cliente-detail/<int:pk> concluído com sucesso.{Cores.RESET}")

    def test_post_clienteCPF(self):
        self.MsgTest = 'Teste do endpoint POST /cliente-create/'
        print(self.MsgTest)
        data = {
            "NomePessoa": "Maria Oliveira",
            "CPFouCNPJ": "309.219.290-72",
            "NomeRua": "Avenida Brasil",
            "Numero": "456",
            "NomeBairro": "Jardim América",
            "Email": "maria.oliveira@example.com",
            "Telefone": "(21)12345-6789",
            "Cidade": "Cianorte"
        }
        response = self.client.post(self.url_create, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 2)
        print(f".{Cores.VERDE}Teste do endpoint POST /cliente-create/ concluído com sucesso.{Cores.RESET}")

    def test_update_clienteCPF(self):
        self.MsgTest = 'Teste do endpoint PUT /cliente-update/<int:pk>'
        print(self.MsgTest)
        data = {
            "NomePessoa": "João Atualizado",
            "CPFouCNPJ": "309.219.290-72",
            "NomeRua": "Rua das Flores",
            "Numero": "123",
            "NomeBairro": "Centro",
            "Email": "joao.silva@example.com",
            "Telefone": "(11)98765-4321",
            "Cidade": "Maringa"
        }
        response = self.client.put(self.url_update, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.NomePessoa, "João Atualizado")
        self.assertEqual(self.cliente.Cidade, "Maringa")
        print(f".{Cores.VERDE}Teste do endpoint PUT /cliente-update/<int:pk> concluído com sucesso.{Cores.RESET}")

    def test_delete_clienteCPF(self):
        self.MsgTest = 'Teste do endpoint DELETE /cliente-delete/<int:pk>'
        print(self.MsgTest)
        response = self.client.delete(self.url_delete)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cliente.objects.count(), 0)
        print(F".{Cores.VERDE}Teste do endpoint DELETE /cliente-delete/<int:pk> concluído com sucesso.{Cores.RESET}")

class ClienteCNPJAPITestCase(APITestCase):
    
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.cliente = Cliente.objects.create(
            NomePessoa="João Silva",
            CPFouCNPJ="91.321.465/0001-08",
            NomeRua="Rua das Flores",
            Numero="123",
            NomeBairro="Centro",
            Email="joao.silva@example.com",
            Telefone="(11)98765-4321",
            Cidade="Cianorte"
        )
        self.url_list = reverse('clientes-list')
        self.url_create = reverse('cliente-create')
        self.url_detail = reverse('cliente-detail', args=[self.cliente.IdPessoa])
        self.url_delete = reverse('cliente-delete', args=[self.cliente.IdPessoa])
        self.url_update = reverse('cliente-update', args=[self.cliente.IdPessoa])

        self.MsgTest = ''

    def test_get_clientesCnpj_list(self):
        self.MsgTest = 'Teste do endpoint GET /clientes/'
        print(self.MsgTest)
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        print(f".{Cores.VERDE}Teste do endpoint GET /clientes/ concluído com sucesso.{Cores.RESET}")

    def test_get_clienteCnpj_detail(self):
        self.MsgTest = 'Teste do endpoint GET /cliente-detail/<int:pk>'
        print(self.MsgTest)
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['NomePessoa'], "João Silva")
        print(f".{Cores.VERDE}Teste do endpoint GET /cliente-detail/<int:pk> concluído com sucesso.{Cores.RESET}")

    def test_post_clienteCnpj(self):
        self.MsgTest = 'Teste do endpoint POST /cliente-create/'
        print(self.MsgTest)
        data = {
            "NomePessoa": "Maria Oliveira",
            "CPFouCNPJ": "73.219.575/0001-73",
            "NomeRua": "Avenida Brasil",
            "Numero": "456",
            "NomeBairro": "Jardim América",
            "Email": "maria.oliveira@example.com",
            "Telefone": "(21)12345-6789",
            "Cidade": "Maringa"
        }
        response = self.client.post(self.url_create, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 2)
        print(f".{Cores.VERDE}Teste do endpoint POST /cliente-create/ concluído com sucesso.{Cores.RESET}")

    def test_update_clienteCnpj(self):
        self.MsgTest = 'Teste do endpoint PUT /cliente-update/<int:pk>'
        print(self.MsgTest)
        data = {
            "NomePessoa": "João Atualizado",
            "CPFouCNPJ": "92.783.810/0001-80",
            "NomeRua": "Rua das Flores",
            "Numero": "123",
            "NomeBairro": "Centro",
            "Email": "joao.silva@example.com",
            "Telefone": "(11)98765-4321",
            "Cidade": "Cianorte"
        }
        response = self.client.put(self.url_update, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.NomePessoa, "João Atualizado")
        self.assertEqual(self.cliente.Cidade, "Cianorte")
        print(f".{Cores.VERDE}Teste do endpoint PUT /cliente-update/<int:pk> concluído com sucesso.{Cores.RESET}")

    def test_delete_clienteCnpj(self):
        self.MsgTest = 'Teste do endpoint DELETE /cliente-delete/<int:pk>'
        print(self.MsgTest)
        response = self.client.delete(self.url_delete)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cliente.objects.count(), 0)
        print(F".{Cores.VERDE}Teste do endpoint DELETE /cliente-delete/<int:pk> concluído com sucesso.{Cores.RESET}")