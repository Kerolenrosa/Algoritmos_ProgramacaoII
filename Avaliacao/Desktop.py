from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self._potenciaDaFonte = potenciaDaFonte

    @property
    def getInformacoes(self):
        return('Potencia da Fonte: ' + self._potenciaDaFonte + '\nModelo: ' + self.modelo + '\nCor: ' + self.cor + '\nPreço: '+self.preco)

    def cadastrar(self):
        pass