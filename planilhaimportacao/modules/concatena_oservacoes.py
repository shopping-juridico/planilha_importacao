import locale

def currency(value):
    if value is None or value == 0:
        return "-"
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    value = locale.currency(value, grouping=True, symbol=None)
    return value

def concatena_observacoes(col_obs: str, col_prob: str, col_prov: int, col_val: int, ws):
    
    for cell in ws[f'{col_obs}']:
        if cell.value == "Observações":
            continue
        cell.value = (f"Probabilidade de Ganho: {ws.cell(row=cell.row, column=col_prob).value} \n"
                     f"Provisão: R$ {currency(ws.cell(row=cell.row, column=col_prov).value)} \n"
                    f"Valor Sentença: R$ {currency(ws.cell(row=cell.row, column=col_val).value)}")
    return ws