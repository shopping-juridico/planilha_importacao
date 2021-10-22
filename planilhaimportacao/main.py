from openpyxl import load_workbook
from modules.valida_coluna import valida_coluna
from modules.classifica_pfpj import classifica_pfpj
from modules.depara import depara_orgao
from modules.valida_num import conta_num
from modules.concatena_titulo import concatena_titulo_pasta

file = 'excel files/importacao.xlsx'

workbook = load_workbook(file)
worksheet = workbook.active

print("------------------------------------------------")
print(" VALIDADOR SJ - PLANILHA DE IMPORTAÇÃO - V0.8  |")
print("------------------------------------------------")
print("O que você quer executar?                      *")
print("                                               *")
print("1 - Validar número de processo                 *")
print("2 - Validar e classificar - CPF/CNPJ Cliente   *")
print("3 - Validar e classificar - CPF/CNPJ Contrário *")
print("4 - Classificar (por nome) - PF/PJ Cliente     *")
print("5 - Classificar (por nome)- PF/PJ Contrário    *")
print("6 - Classificar - Órgãos                       *")
print("7 - Concatenar Título com pasta                *")
print("8 - Tudo                                       *")
print("************************************************")

opcao = 0
while opcao != 1 and opcao != 2 and opcao !=3 and opcao !=4 and opcao !=5 and opcao !=6 and opcao !=7 and opcao !=8:
    opcao = int(input("Opção: "))
    print("----------------------------------------------")
    if opcao != 1 and opcao != 2 and opcao !=3 and opcao !=4 and opcao !=5 and opcao !=6 and opcao !=7 and opcao !=8:
        print("Opção inválida! Tente novamente.")

if opcao == 1:
    conta_num('D', 18, worksheet)
    print()
    print("Números CNJ e antigo identificados")
if opcao == 2:
    valida_coluna(pam2='M', pam3=14, ws=worksheet)
    print()
    print("CPF/CNPJ de clientes validados!")
if opcao == 3:
    valida_coluna(pam2='P', pam3=17, ws=worksheet)
    print()
    print("CPF/CNPJ de contrários validados!")    
if opcao == 4:
    classifica_pfpj(pam1='K', pam2=14, ws=worksheet)
    print()
    print("Clientes classificados em PF/PJ!")
if opcao == 5:
    classifica_pfpj(pam1='O', pam2=17, ws=worksheet)
    print()
    print("Contrários classificados em PF/PJ!")
if opcao == 6:
    ...
    # depara_orgao(pam3="Y", ws=worksheet)
    # print()
    # print("Órgãos classificados!")
if opcao == 7:
    concatena_titulo_pasta('U', 31, worksheet)
    print()
    print("Títulos concatenados com pasta")

if opcao == 8:
    conta_num('D', 18, worksheet)
    valida_coluna(pam2='M', pam3=14, ws=worksheet)
    valida_coluna(pam2='P', pam3=17, ws=worksheet)
    classifica_pfpj(pam1='K', pam2=14, ws=worksheet)
    classifica_pfpj(pam1='O', pam2=17, ws=worksheet)
    #depara_orgao(pam3="Y", ws=worksheet)
    concatena_titulo_pasta('U', 31, worksheet)

workbook.save("excel files/importacao_format.xlsx")