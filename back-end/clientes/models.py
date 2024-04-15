from django.db import models

class Cliente(models.Model):
    IdPessoa = models.AutoField(primary_key=True)
    NomePessoa = models.CharField(blank=False, max_length=255)
    CPF = models.CharField(blank=False, max_length=14)
    NomeRua = models.CharField(blank=False, max_length=255)
    Numero = models.CharField(blank=False, max_length=10)
    NomeBairro = models.CharField(blank=False, max_length=255)
    Email = models.EmailField(blank=False, max_length=255)
    Telefone = models.CharField(blank=False, max_length=14)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['IdPessoa']

    def __str__(self):
        return self.NomePessoa