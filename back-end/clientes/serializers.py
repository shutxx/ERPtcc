from rest_framework import serializers
from .models import Cliente
from .utils import valida_cpf, validar_cnpj
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
        elif validar_cnpj(documento):
            is_valid = True
        else:
            raise serializers.ValidationError('CPF ou CNPJ inválido.')

        if not self.instance and Cliente.objects.filter(CPFouCNPJ=documento).exists():
            raise serializers.ValidationError('Já existe um cliente com este documento.')
        
        return documento
    
    def validate_Telefone(self, telefone):
        if not re.match(r'^\(?(\d{2})\)? ?\d{4,5}-\d{4}$', telefone):
            raise serializers.ValidationError('Telefone inválido.')
        return telefone