from rest_framework import serializers
from .models import ContaPagar, ContaReceber, EstornoLog

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
            'Status',
            'Estornada'
        ]

class EstornoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstornoLog
        fields = [
            'IdVenda',
            'DataEstorno',
            'Motivo'
        ]