from rest_framework import serializers
from .models import Fornecedor

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