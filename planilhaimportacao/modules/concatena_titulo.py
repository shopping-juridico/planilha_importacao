def concatena_titulo_pasta(col_tit: str, col_pas: int, ws):
    
    for cell in ws[f'{col_tit}']:
        if cell.value == "Título":
            continue
        if cell.value is None:
            cell.value = f"Pasta: {ws.cell(row=cell.row, column=col_pas).value}"
        else:
            cell.value = f"Pasta: {ws.cell(row=cell.row, column=col_pas).value} \n{cell.value}"
    
    return ws