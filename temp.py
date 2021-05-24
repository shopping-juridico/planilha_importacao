class Cnpj:
    
    def __init__(self, documento):
        documento = str(documento)
        if self.cnpj_eh_Valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ Inválido")
    
    
    def cnpj_eh_Valido(self, documento):
        if len(documento) == 14:
            return True
        else:
            return False