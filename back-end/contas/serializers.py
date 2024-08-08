from rest_framework import serializers
from .models import ContaPagar, ContaReceber

class ContaPagarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContaPagar
        fields = [
            'IdContaPagar',
            'IdCompra',
            'Valor',
            'DataVencimento',
            'DataEntrada',
            'Status'
        ]

class ContaReceberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContaReceber
        fields = [
            'IdContaReceber',
            'IdVenda',
            'Valor',
            'DataEntrada',
            'DataVencimento',
            'Status'
        ]