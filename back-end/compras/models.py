from django.db import models
from fornecedores.models import Fornecedor
from produtos.models import Produto

class Compra(models.Model):
    IdCompra = models.AutoField(primary_key=True)
    IdFornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    DataCompra = models.DateField(blank=False)
    ValorTotal = models.FloatField(blank=False, max_length=10)
    Prazo = models.CharField(blank=False, max_length=15, default='default')
    Parcelas = models.IntegerField(blank=False, default=1)
    FormaPagamento = models.CharField(blank=False, max_length=15, default='default')
    
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['IdCompra']

    def __str__(self):
        return self.IdCompra

class ItensCompra(models.Model):
    IdItensCompra = models.AutoField(primary_key=True)
    IdCompra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens_compra')
    IdProduto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    NomeProduto = models.CharField(blank=False, max_length=255, default='default')
    ValorUnitario = models.FloatField(blank=False, max_length=10)
    QtdProduto = models.IntegerField(blank=False)
    ValorTotal = models.FloatField(blank=False, max_length=10)

    class Meta:
        verbose_name = 'ItenCompra'
        verbose_name_plural = 'ItensCompra'
        ordering = ['IdItensCompra']

    def __str__(self):
        return self.IdItensCompra