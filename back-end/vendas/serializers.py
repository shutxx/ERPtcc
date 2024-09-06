from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Venda, ItensVenda
from datetime import datetime, timedelta
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer
from contas.models import ContaReceber
from produtos.models import Produto

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

class VendaContaSerializer(serializers.ModelSerializer):
    IdCliente = ClienteSerializer(read_only=True)
    
    class Meta:
        model = Venda
        fields = [
            'IdVenda',
            'DataVenda',
            'TotalVenda',
            'FormaPagamento',
            'Prazo',
            'IdCliente',
            'Parcelas',
        ] 

class VendaSerializer(serializers.ModelSerializer):
    IdCliente = ClienteSerializer(read_only=True)
    itens_venda = ItensVendaSerializer(many=True)

    class Meta:
        model = Venda
        fields = [
            'IdVenda',
            'DataVenda',
            'TotalVenda',
            'FormaPagamento',
            'Prazo',
            'Parcelas',
            'IdCliente',
            'itens_venda'
        ] 

    def create(self, validated_data):

        prazo = validated_data['Prazo'].split(',')
        parcelas = validated_data['Parcelas']
        total_venda = validated_data['TotalVenda']
        valor_parcela = total_venda / parcelas
        data_entrada = datetime.now().date()

        if len(prazo) != parcelas:
            raise ValidationError("O número de prazos deve ser igual ao número de parcelas.")

        data_venda = validated_data.get('DataVenda')
        if isinstance(data_venda, str):
            data_venda = datetime.strptime(data_venda, "%Y-%m-%d").date()

        itens_venda_data = validated_data.pop('itens_venda')
        cliente_id = self.initial_data.get('IdCliente')

        cliente = Cliente.objects.get(pk=cliente_id)
        
        venda = Venda.objects.create(IdCliente=cliente, **validated_data)
        for item_data in itens_venda_data:
            item = ItensVenda.objects.create(IdVenda=venda, **item_data)

            nome = item.NomeProduto
            produto_id = item.IdProduto.IdProduto
            quantidade = item.QtdProduto

            qtd = Produto.objects.get(IdProduto=produto_id)
            qtd.remover_quantidade(nome , quantidade)

        contador_parcela = 1
        for dias in prazo:
            data_vencimento = data_venda + timedelta(days=int(dias))
            ContaReceber.objects.create(
                IdVenda=venda,
                Valor=valor_parcela,
                DataVencimento=data_vencimento,
                DataEntrada=data_entrada,
                Status=False
            )
            contador_parcela += 1
            
        return venda
    
    def update(self, instance, validated_data):
        itens_venda_data = validated_data.pop('itens_venda')
        cliente_id = self.initial_data.get('IdCliente')
        
        if cliente_id:
            cliente = Cliente.objects.get(pk=cliente_id)
            instance.IdCliente = cliente
            instance.save()
        
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