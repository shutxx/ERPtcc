from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            'IdProduto',
            'NomeProduto',
            'Descricao',
            'Preco',
            'PrecoCompra',
            'UnidMedida',
            'Estoque'
        ]