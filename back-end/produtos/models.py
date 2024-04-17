from django.db import models

class Produto(models.Model):
    IdProduto = models.AutoField(primary_key=True)
    NomeProduto = models.CharField(blank=False, max_length=255)
    Descricao = models.CharField(blank=False, max_length=255)
    Preco = models.FloatField(blank=False, max_length=10)
    UnidMedida = models.CharField(blank=False, max_length=20)
    Estoque = models.IntegerField(blank=False)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['IdProduto']

    def __str__(self):
        return self.NomeProduto