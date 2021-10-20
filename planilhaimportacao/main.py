from openpyxl import load_workbook
from modules.valida_coluna import valida_coluna
from modules.classifica_pfpj import classifica_pfpj
from modules.depara import depara_orgao

file = 'excel files/importacao.xlsx'

workbook = load_workbook(file)
worksheet = workbook.active

print("----------------------------------------------")
print("VALIDADOR SJ - PLANILHA DE IMPORTAÇÃO - V0.6 |")
print("----------------------------------------------")
print("O que você quer executar?                    *")
print("                                             *")
print("1 - Validar - CPF/CNPJ Cliente               *")
print("2 - Validar - CPF/CNPJ Contrário             *")
print("3 - Classificar - PF/PJ Cliente              *")
print("4 - Classificar - PF/PJ Contrário            *")
print("5 - Classificar - Órgãos                     *")
print("6 - Tudo                                     *")
print("**********************************************")

opcao = 0
while opcao != 1 and opcao != 2 and opcao !=3 and opcao !=4 and opcao !=5 and opcao !=6:
    opcao = int(input("Opção: "))
    print("----------------------------------------------")
    if opcao != 1 and opcao != 2 and opcao !=3 and opcao !=4 and opcao !=5 and opcao !=6:
        print("Opção inválida! Tente novamente.")

if opcao == 1:
    valida_coluna(pam2='M', ws=worksheet)
    print()
    print("CPF/CNPJ de clientes validados!")
if opcao == 2:
    valida_coluna(pam2='P', ws=worksheet)
    print()
    print("CPF/CNPJ de contrários validados!")    
if opcao == 3:
    classifica_pfpj(pam1='K', pam2=14, ws=worksheet)
    print()
    print("Clientes classificados em PF/PJ!")
if opcao == 4:
    classifica_pfpj(pam1='O', pam2=17, ws=worksheet)
    print()
    print("Contrários classificados em PF/PJ!")
if opcao == 5:
    depara_orgao(pam3="Y", ws=worksheet)
    print()
    print("Órgãos classificados!") 
if opcao == 6:
    valida_coluna(pam2='M', ws=worksheet)
    valida_coluna(pam2='P', ws=worksheet)
    classifica_pfpj(pam1='K', pam2=14, ws=worksheet)
    classifica_pfpj(pam1='O', pam2=17, ws=worksheet)
    depara_orgao(pam3="Y", ws=worksheet)

workbook.save("excel files/importacao_format.xlsx")