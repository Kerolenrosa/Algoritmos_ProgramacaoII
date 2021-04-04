from Veiculo import Veiculo

class Automovel (Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor):
        
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        
        self.potenciaDoMotor = potenciaDoMotor
       

    def imprimir (self):
        print ("O veiculo", self.marca, "tem a quantidade de" , self.qtdRodas, "rodas, possui o modelo" ,self.modelo, "e a velocidade inicial é" , self.velocidade, "km/h com potência de" ,self.potenciaDoMotor,"de motor.")
