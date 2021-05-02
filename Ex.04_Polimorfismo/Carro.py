from Automovel import Automovel

class Carro (Automovel):
    def __init__ (self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, qtdPortas):
        
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        
        self.qtdPortas = qtdPortas

    def imprimir (self):
        print ("O veiculo", self.marca, "tem a quantidade de" , self.qtdRodas, "rodas, possui o modelo" ,self.modelo, "e a velocidade inicial é" , self.velocidade, "km/h com", self.potenciaDoMotor, "de potência do motor e com", self.qtdPortas,"portas.")