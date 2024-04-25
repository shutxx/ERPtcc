from rest_framework import serializers
from .models import Compra, ItensCompra

class ItensCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = [
            'IdItensCompra',
            'IdProduto',
            'ValorUnitario',
            'QtdProduto',
            'ValorTotal'
        ]

class CompraSerializer(serializers.ModelSerializer):
    itens_compra = ItensCompraSerializer(many=True)
    
    class Meta:
        model = Compra
        fields = [
            'IdCompra',
            'IdFornecedor',
            'DataCompra',
            'ValorTotal',
            'itens_compra'
        ]

    def create(self, validated_data):
        itens_compra_data = validated_data.pop('itens_compra')
        compra = Compra.objects.create(**validated_data)  

        for item_data in itens_compra_data:
            ItensCompra.objects.create(IdCompra=compra, **item_data)

        return compra

    
