from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.__tempoDeBateria = tempoDeBateria

    @property
    def getInformacoes(self):
        return('Tempo de bateria: ' + self.__tempoDeBateria + '\nModelo: ' + self.modelo + '\nCor: ' + self.cor + '\nPreço: '+self.preco)


    def cadastrar(self):
        pass