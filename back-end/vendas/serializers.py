from rest_framework import serializers
from .models import Venda, ItensVenda

class ItensVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensVenda
        fields = [
            'IdItensVenda',
            'IdVenda',
            'IdProduto',
            'QtdProduto',
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

    def create_venda(self, itens_venda):
        itens_venda_data = itens_venda.pop('itens_venda')
        venda = Venda.objects.create(**itens_venda)
        for item_data in itens_venda_data: 
            ItensVenda.objects.create(IdVenda=venda, **item_data)  
        return venda