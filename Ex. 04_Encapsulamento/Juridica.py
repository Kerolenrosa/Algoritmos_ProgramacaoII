from Exercicio_encapsulamento.Pessoa import Pessoa

class Juridica():
    def __init__(self, cnpj, inscricaoEstatudal, quantidadeFuncionarios):
        self.__cnpj = cnpj
        self.__inscricaoEstatudal = inscricaoEstatudal
        self.quantidadeFuncionarios = quantidadeFuncionarios

    def imprimeCNPJ(self):
        print("CNPJ cadastrado: ", self.__cnpj)


    def __emitirNotaFiscal(self):
        print('Nota fiscal Emitida')

    def GetNotaFiscal(self):
        self.__emitirNotaFiscal()