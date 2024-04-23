from django.db import models
from clientes.models import Cliente
from produtos.models import Produto

class Venda(models.Model):
    IdVenda = models.AutoField(primary_key=True)
    IdCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    DataVenda = models.DateField(blank=False)
    TotalVenda = models.FloatField(blank=False, max_length=10)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
        ordering = ['IdVenda']

    def __str__(self):
        return self.IdVenda

class ItensVenda(models.Model):
    IdItensVenda = models.AutoField(primary_key=True)
    IdVenda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens_venda')
    IdProduto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    QtdProduto = models.IntegerField(blank=False)
    ValorUnitario = models.FloatField(blank=False, max_length=10)
    ValorTotal = models.FloatField(blank=False, max_length=10)

    class Meta:
        verbose_name = 'ItenVenda'
        verbose_name_plural = 'ItensVenda'
        ordering = ['IdItensVenda']

    def __str__(self):
        return self.IdItensVenda