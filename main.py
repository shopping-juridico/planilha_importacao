from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import Color, PatternFill
from validacpf import ValidaCpf
from validacnpj import ValidaCnpj

wb = load_workbook('Importação de processos (Aberto) Corrigido.xlsx')

ws = wb.active

redFill = PatternFill(start_color='FFFF0000',
                   end_color='FFFF0000',
                   fill_type='solid')

# pf/pj
def valida_coluna(pam):
    
    for cell in ws['{}'.format(pam)]:
        if(cell.value is not None):
            if cell.value == "Contrário Principal - CPF/CNPJ":
                continue
            if cell.value == "Cliente principal - CPF/CNPJ":
                continue
            cpf = ValidaCpf(cell.value)
            cnpj = ValidaCnpj(cell.value)
            if cpf.valida():
                a = 2
                #print('CPF válido')
                #print(cell.value)
            elif cnpj.valida():
                a = 3
                #print('CNPJ válido')
                #print(cell.value)
            else:
                cell.fill = redFill
                print('CPF inválido')
        #else:

def main():
    valida_coluna(pam='S')
    valida_coluna(pam='P')

main()

wb.save("/home/vitor/projetos/planilha_importacao/importacao_format.xlsx")