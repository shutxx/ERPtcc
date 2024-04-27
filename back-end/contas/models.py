from django.db import models
from clientes.models import Cliente
from fornecedores.models import Fornecedor

class Conta(models.Model):
    Valor = models.DecimalField(max_digits=10, decimal_places=2)
    DataVencimento = models.DateField()
    DataPagamento = models.DateField(blank=True, null=True)
    Pago = models.BooleanField(default=False)

class ContaPagar(Conta):
    IdContaPagar = models.AutoField(primary_key=True)
    IdFornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ContaPagar'
        verbose_name_plural = 'ContasPagar'
        ordering = ['IdContaPagar']

    def __str__(self):
        return self.IdContaPagar

class ContaReceber(Conta):
    IdContaReceber = models.AutoField(primary_key=True)
    IdCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ContaReceber'
        verbose_name_plural = 'ContasReceber'
        ordering = ['IdContaReceber']

    def __str__(self):
        return self.IdContaReceber