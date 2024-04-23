from rest_framework import serializers
from .models import Venda, ItensVenda

class ItensVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensVenda
        fields = [
            'IdItensVenda',
            'IdProduto',
            'QtdProduto',
            'NomeProduto',
            'ValorUnitario',
            'ValorTotal'
        ]

class VendaSerializer(serializers.ModelSerializer):
    itens_venda = ItensVendaSerializer(many=True)

    class Meta:
        model = Venda
        fields = [
            'IdVenda',
            'IdCliente',
            'DataVenda',
            'TotalVenda',
            'itens_venda' 
        ]

    def create(self, validated_data):
        itens_venda_data = validated_data.pop('itens_venda')
        venda = Venda.objects.create(**validated_data)
        for item_data in itens_venda_data:
            ItensVenda.objects.create(IdVenda=venda, **item_data)
        return venda
