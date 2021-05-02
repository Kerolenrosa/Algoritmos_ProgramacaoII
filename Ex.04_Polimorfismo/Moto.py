from Automovel import Automovel

class Moto (Automovel):
    def __init__ (self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, partidaEletrica):
        
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        
        self.partidaEletrica = partidaEletrica

    def imprimir (self):
        print ("O veiculo", self.marca, "tem a quantidade de" , self.qtdRodas, "rodas, possui o modelo" ,self.modelo, "e a velocidade inicial é" , self.velocidade, "km/h com potência de", self.potenciaDoMotor, "do motor e", self.partidaEletrica, "partida elétrica.")
