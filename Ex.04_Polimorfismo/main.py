from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel
from Moto import Moto
from Carro import Carro

v1 = Veiculo("Renault", 4, "Logan", 30)
b1 = Bicicleta("Caloi", 2, "Caloi 10", 5, 24, 1)
a1 = Automovel("Citroen" , 4, "C3", 20, "1.0 turbo")
m1 = Moto("Honda",2,"CG 160 Titan S",45, "15,1 CV", "possui" )
c1 = Carro("Chevrolet" , 4, "Cruze", 60, "1.4 turbo", "5")

v1.imprimir ()
v1.acelerar(15)
v1.imprimir()
v1.frear(5)
v1.imprimir()
b1.imprimir()
a1.imprimir()
m1.imprimir()
c1.imprimir()