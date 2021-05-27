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

def verifica_pessoa(pam2):         
    for cell in ws['{}'.format(pam2)]:
        if cell.value is None:    
            for ws.cell(cell.row,14) in ws['N']:
                if 'S/A' in cell.value:
                    #print(cell.value)        
                    cell.fill = redFill
                elif 'LTDA' in cell.value:
                    #print(cell.value)        
                    cell.fill = redFill
                elif 'CIA' in cell.value:
                    #print(cell.value)        
                    cell.fill = redFill
                elif 'COMPANH' in cell.value:
                    #print(cell.value)        
                    cell.fill = redFill
                elif 'COND' in cell.value:
                    #print(cell.value)        
                    cell.fill = redFill
                elif 'ASSOCI' in cell.value:
                    #print(cell.value)        
                    cell.fill = redFill
                elif 'SEGUR' in cell.value:
                    #print(cell.value)        
                    cell.fill = redFill 
                elif '-' in cell.value:
                    #print(cell.value)        
                    cell.fill = redFill
                elif 'INSTI' in cell.value:
                    #print(cell.value)        
                    cell.fill = redFill                      
                elif 'ADVO' in cell.value:
                    #print(cell.value)        
                    cell.fill = redFill 

def main():
    #valida_coluna(pam='P')
    #valida_coluna(pam='S')
    verifica_pessoa(pam2='P')

main()

wb.save("/home/vitor/projetos/planilha_importacao/importacao_format.xlsx")