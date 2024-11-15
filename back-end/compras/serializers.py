from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Compra, ItensCompra
from datetime import datetime, timedelta
from .models import Fornecedor
from fornecedores.serializers import FornecedorSerializer
from contas.models import ContaPagar
from produtos.models import Produto


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

class CompraContaSerializer(serializers.ModelSerializer):
    IdFornecedor = FornecedorSerializer(read_only=True)
    
    class Meta:
        model = Compra
        fields = [
            'IdCompra',
            'DataCompra',
            'ValorTotal',
            'FormaPagamento',
            'Prazo',
            'Parcelas',
            'IdFornecedor'
        ]

class CompraSerializer(serializers.ModelSerializer):
    IdFornecedor = FornecedorSerializer(read_only=True)
    itens_compra = ItensCompraSerializer(many=True)
    
    class Meta:
        model = Compra
        fields = [
            'IdCompra',
            'DataCompra',
            'ValorTotal',
            'FormaPagamento',
            'Prazo',
            'Parcelas',
            'IdFornecedor',
            'itens_compra'
        ]

    def create(self, validated_data):

        prazo = validated_data['Prazo'].split(',')
        parcelas = validated_data['Parcelas']
        total_compra = validated_data['ValorTotal']
        valor_parcela = total_compra / parcelas
        data_entrada = datetime.now().date()

        if len(prazo) != parcelas:
            raise ValidationError("O número de prazos deve ser igual ao número de parcelas.")
        
        data_venda = validated_data.get('DataCompra')
        if isinstance(data_venda, str):
            data_venda = datetime.strptime(data_venda, "%Y-%m-%d").date()

        itens_compra_data = validated_data.pop('itens_compra')
        fornecedor_id = self.initial_data.get('IdFornecedor')
        
        fornecedor = Fornecedor.objects.get(pk=fornecedor_id)

        compra = Compra.objects.create(IdFornecedor=fornecedor, **validated_data)
        for item_data in itens_compra_data:
            item = ItensCompra.objects.create(IdCompra=compra, **item_data)

            produto_id = item.IdProduto.IdProduto
            quantidade = item.QtdProduto

            qtd = Produto.objects.get(IdProduto=produto_id)
            qtd.adicionar_quantidade(quantidade)

        contador_parcela = 1
        for dias in prazo:
            data_vencimento = data_venda + timedelta(days=int(dias))
            ContaPagar.objects.create(
                IdCompra=compra,
                Valor=valor_parcela,
                DataVencimento=data_vencimento,
                DataEntrada=data_entrada,
                Status=False
            )
            contador_parcela += 1

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
