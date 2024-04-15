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