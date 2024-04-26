from rest_framework import serializers
from .models import Compra, ItensCompra

class ItensCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = [
            'IdItensCompra',
            'IdProduto',
            'NomeProduto',
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
    
    def update(self, instance, validated_data):
        itens_compra_data = validated_data.pop('itens_compra')
        instance = super().update(instance, validated_data)

        itens_compra_ids = [item_data.get('IdItensCompra') for item_data in itens_compra_data]
        instance.itens_compra.all().exclude(IdItensCompra__in=itens_compra_ids).delete()

        for item_data in itens_compra_data:
            IdItensCompra = item_data.get('IdItensCompra')
            if IdItensCompra:
                item = ItensCompra.objects.filter(IdItensCompra=IdItensCompra, IdCompra=instance).first()
                if item:
                    for attr, value in item_data.items():
                        setattr(item, attr, value)
                    item.save()
            else:
                ItensCompra.objects.create(IdCompra=instance, **item_data)

        return instance
