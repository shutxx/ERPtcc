from rest_framework import serializers
from .models import ContaPagar, ContaReceber

class ContaPagarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContaPagar
        fields = [
            'IdContaPagar',
            'IdFornecedor',
            'Valor',
            'DataVencimento',
            'DataPagamento',
            'Pago'
        ]

class ContaReceberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContaReceber
        fields = [
            'IdContaReceber',
            'IdCliente',
            'Valor',
            'DataVencimento',
            'DataPagamento',
            'Pago'
        ]