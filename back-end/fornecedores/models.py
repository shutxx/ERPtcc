from django.db import models

class Fornecedor(models.Model):
    IdFornecedor = models.AutoField(primary_key=True)
    NomeFantasia = models.CharField(blank=False, max_length=255)
    NomeJuridico = models.CharField(blank=False, max_length=255)
    CNPJ = models.CharField(blank=False, max_length=18)
    NomeRua = models.CharField(blank=False, max_length=255)
    Numero = models.CharField(blank=False, max_length=10)
    NomeBairro = models.CharField(blank=False, max_length=255)
    Email = models.EmailField(blank=False, max_length=255)
    Telefone = models.CharField(blank=False, max_length=14)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['IdFornecedor']

    def __str__(self):
        return self.NomeFantasia