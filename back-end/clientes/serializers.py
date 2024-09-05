from rest_framework import serializers
from .models import Cliente
from utils.util import valida_cnpj, valida_Telefone, valida_cpf
import re

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'IdPessoa',
            'NomePessoa',
            'Email',
            'Telefone',
            'CPFouCNPJ',
            'NomeRua',
            'Numero',
            'NomeBairro'
        ]

    def validate_CPFouCNPJ(self, documento):
        if valida_cpf(documento):
            is_valid = True
        elif valida_cnpj(documento):
            is_valid = True
        else:
            raise serializers.ValidationError('CPF ou CNPJ inválido.')

        if not self.instance and Cliente.objects.filter(CPFouCNPJ=documento).exists():
            raise serializers.ValidationError('Já existe um cliente com este documento.')
        
        return documento
    
    def validate_Telefone(self, telefone):
        telefone = telefone.strip()
        if valida_Telefone(telefone):
            return True
        else:
            raise serializers.ValidationError('Telefone inválido.')