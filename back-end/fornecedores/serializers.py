from rest_framework import serializers
from .models import Fornecedor
from .utils import valida_cnpj
import re

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = [
            'IdFornecedor',
            'NomeFantasia',
            'NomeJuridico', 
            'Email', 
            'Telefone',
            'CNPJ', 
            'NomeRua', 
            'Numero', 
            'NomeBairro' 
        ]

    def validate_CNPJ(self, cnpj):
        if not valida_cnpj(cnpj):
            raise serializers.ValidationError('CNPJ inválido')
        if self.instance:
            return cnpj
        if Fornecedor.objects.filter(CNPJ=cnpj).exists():
            raise serializers.ValidationError('Já existe um fornecedor com este CNPJ')
        return cnpj
    
    def validate_Telefone(self, telefone):
        if not re.match(r'^\(?(\d{2})\)? ?\d{4,5}-\d{4}$', telefone):
            raise serializers.ValidationError('Telefone inválido.')
        return telefone
    