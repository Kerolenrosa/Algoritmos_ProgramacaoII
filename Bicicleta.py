from Veiculo import Veiculo

class Bicicleta (Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, numMarchas, bagageiro):
        
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimir (self):
        print ("O veiculo", self.marca, "tem a quantidade de" , self.qtdRodas, "rodas, possui o modelo" ,self.modelo, "e a velocidade inicial é" , self.velocidade, "km/h com", self.numMarchas, "marchas e com", self.bagageiro,"bagageiro (s).")
