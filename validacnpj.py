import re
from sre_constants import FAILURE

class ValidaCnpj:

    def __init__(self, cnpj):
        self.cnpj = cnpj
        #print(self.cnpj)

    def valida(self):
        if not self.cnpj:
            return False
        
        novo_cnpj = self._calcula_digitos(self.cnpj[:12], multiplicador_inicial=5)
        novo_cnpj = self._calcula_digitos(novo_cnpj, multiplicador_inicial=6)

        if novo_cnpj == self.cnpj:
            return True
        return False    
    
    @staticmethod
    def _calcula_digitos(fatia_cnpj, multiplicador_inicial):
        if not fatia_cnpj:
            return False
        
        sequencia = fatia_cnpj[0] * len(fatia_cnpj) #primeiro caractere
        
        if sequencia == fatia_cnpj:
            return False

        soma = 0
        for chave, _ in enumerate(range(len(fatia_cnpj)+1, 1, -1)):
            soma += int(fatia_cnpj[chave]) * multiplicador_inicial

            if (multiplicador_inicial == 2):
                multiplicador_inicial = 9
            else:
                multiplicador_inicial -= 1
    
        resto = 11 - (soma%11)
        resto = resto if resto <= 9 else 0
        
        return fatia_cnpj + str(resto) #concatenar

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self._cnpj = self._so_numeros(cnpj)
    
    @staticmethod
    def _so_numeros(cnpj):
        return re.sub('[^0-9]', '', cnpj)