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
    
    def update(self, instance, validated_data):
        itens_venda_data = validated_data.pop('itens_venda')
        instance = super().update(instance, validated_data)

        itens_venda_ids = [item_data.get('IdItensVenda') for item_data in itens_venda_data]
        instance.itens_venda.all().exclude(IdItensVenda__in=itens_venda_ids).delete()

        for item_data in itens_venda_data:
            IdItensVenda = item_data.get('IdItensVenda')
            if IdItensVenda:
                item = ItensVenda.objects.filter(IdItensVenda=IdItensVenda, IdVenda=instance).first()
                if item:
                    for attr, value in item_data.items():
                        setattr(item, attr, value)
                    item.save()
            else:
                ItensVenda.objects.create(IdVenda=instance, **item_data)

        return instance