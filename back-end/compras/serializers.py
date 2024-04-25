from rest_framework import serializers
from .models import Compra, ItensCompra

class ItensCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = [
            'IdItensCompra',
            'IdCompra',
            'IdProduto',
            'ValorUnitario',
            'QtdProduto',
            'ValorTotal'
        ]

class CompraSerializer(serializers.ModelSerializer):
    Itens_Compra = ItensCompraSerializer(many=True)
    
    class Meta:
        model = Compra
        fields = [
            'IdCompra',
            'IdFornecedor',
            'DataCompra',
            'ValorTotal',
            'Itens_Compra'
        ]