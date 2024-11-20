from django.db import models
from vendas.models import Venda
from compras.models import Compra

class EstornoLog(models.Model):
    IdVenda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    DataEstorno = models.DateTimeField(auto_now_add=True)
    Motivo = models.TextField()

    def __str__(self):
        return self.IdVenda

class Conta(models.Model):
    Valor = models.DecimalField(max_digits=10, decimal_places=2)
    DataVencimento = models.DateField()
    DataEntrada = models.DateField(blank=True, null=True)
    Status = models.BooleanField(default=False)
    Estornada = models.BooleanField(default=False)

class ContaPagar(Conta):
    IdContaPagar = models.AutoField(primary_key=True)
    IdCompra = models.ForeignKey(Compra, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ContaPagar'
        verbose_name_plural = 'ContasPagar'
        ordering = ['IdContaPagar']

    def __str__(self):
        return self.IdContaPagar

class ContaReceber(Conta):
    IdContaReceber = models.AutoField(primary_key=True)
    IdVenda = models.ForeignKey(Venda, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ContaReceber'
        verbose_name_plural = 'ContasReceber'
        ordering = ['IdContaReceber']

    def __str__(self):
        return self.IdContaReceber