from modules.valida_coluna import valida_coluna
from modules.classifica_pfpj import classifica_pfpj
from modules.depara import depara_orgao

print("----------------------------------------------")
print("VALIDADOR SJ - PLANILHA DE IMPORTAÇÃO - V0.6 |")
print("----------------------------------------------")
print("O que você quer executar?                    *")
print("                                             *")
print("1 - Validar - CPF/CNPJ Cliente               *")
print("2 - Validar - CPF/CNPJ Contrário             *")
print("3 - Classificar - PF/PJ Cliente              *")
print("4 - Classificar - Órgãos                     *")
print("5 - Tudo                                     *")
print("**********************************************")

opcao = 0
while opcao != 1 and opcao != 2 and opcao !=3 and opcao !=4 and opcao !=5:
    opcao = int(input("Opção: "))
    print("----------------------------------------------")
    if opcao != 1 and opcao != 2 and opcao !=3 and opcao !=4 and opcao !=5:
        print("Opção inválida! Tente novamente.")

if opcao == 1:
    valida_coluna(pam2='P')
    print()
    print("CPF/CNPJ de clientes validados!")
if opcao == 2:
    valida_coluna(pam2='S')
    print()
    print("CPF/CNPJ de contrários validados!")    
if opcao == 3:
    classifica_pfpj(pam1='N')
    print()
    print("Clientes classificados em PF/PJ!")
if opcao == 4:
    depara_orgao(pam3="Y")
    print()
    print("Órgãos classificados!") 
if opcao == 5:
    valida_coluna(pam2='P')
    valida_coluna(pam2='S')
    classifica_pfpj(pam1='N')
    depara_orgao(pam3="Y")

