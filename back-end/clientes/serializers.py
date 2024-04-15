from rest_framework import serializers
from .models import Cliente
from .utils import valida_cpf
import re

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'IdPessoa',
            'NomePessoa',
            'Email',
            'Telefone',
            'CPF',
            'NomeRua',
            'Numero',
            'NomeBairro'
        ]

    def validate_CPF(self, cpf):
        if not valida_cpf(cpf):
            raise serializers.ValidationError('CPF inválido.')
        if Cliente.objects.filter(CPF=cpf).exists():
            raise serializers.ValidationError('Já existe um cliente com este CPF.')
        return cpf
    
    def validate_Telefone(self, telefone):
        if not re.match(r'^\(?(\d{2})\)? ?\d{4,5}-\d{4}$', telefone):
            raise serializers.ValidationError('Telefone inválido.')
        return telefone