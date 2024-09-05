from rest_framework import serializers
import re

def valida_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = 11 - (soma % 11)
    digito_1 = resto if resto < 10 else 0
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = 11 - (soma % 11)
    digito_2 = resto if resto < 10 else 0
    
    return cpf[-2:] == str(digito_1) + str(digito_2)

def valida_cnpj(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))
    if len(cnpj) != 14:
        return False
    if cnpj == cnpj[0] * 14:
        return False
    soma = 0
    peso = 5
    for num in cnpj[:12]:
        soma += int(num) * peso
        peso -= 1
        if peso == 1:
            peso = 9
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0
    soma = 0
    peso = 6
    for num in cnpj[:13]:
        soma += int(num) * peso
        peso -= 1
        if peso == 1:
            peso = 9
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    return int(cnpj[12]) == digito1 and int(cnpj[13]) == digito2

def valida_Telefone(telefone):
    pattern = r'^\(\d{2}\)\d{5}-\d{4}$'
    return bool(re.match(pattern, telefone))