from validacnpj import ValidaCnpj

cnpj = ValidaCnpj('38.699.342/0001-14')

if cnpj.valida():
    print('CNPJ válido')
else:
    print('CNPJ inválido')