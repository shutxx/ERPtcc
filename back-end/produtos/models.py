from django.db import models
from rest_framework.exceptions import ValidationError

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
    
    def adicionar_quantidade(self, quantidade):
        self.Estoque += quantidade
        self.save()

    def remover_quantidade(self,  nome, quantidade):
        if quantidade > self.Estoque:
            raise ValidationError(f"Quantidade insuficiente em estoque para {nome}")
        self.Estoque -= quantidade
        self.save()