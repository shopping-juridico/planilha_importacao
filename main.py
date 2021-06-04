from modules.valida_coluna import valida_coluna
from modules.classifica_pfpj import classifica_pfpj

print("----------------------------------------------")
print("VALIDADOR SJ - PLANILHA DE IMPORTAÇÃO - V0.6 |")
print("----------------------------------------------")
print("O que você quer validar?                     *")
print("                                             *")
print("1 - CPF/CNPJ - Cliente                       *")
print("2 - CPF/CNPJ - Contrário                     *")
print("3 - Classificar PF/PJ - Cliente              *")
print("4 - Tudo                                     *")
print("**********************************************")

opcao = 0
while opcao != 1 and opcao != 2 and opcao !=3 and opcao !=4:
    opcao = int(input("Opção: "))
    print("----------------------------------------------")
    if opcao != 1 and opcao != 2 and opcao !=3 and opcao !=4:
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
    valida_coluna(pam2='P')
    valida_coluna(pam2='S')
    classifica_pfpj(pam1='N')

