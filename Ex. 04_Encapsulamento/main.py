from Exercicio_encapsulamento.Pessoa import Pessoa
from Exercicio_encapsulamento.Fisica import Fisica
from Exercicio_encapsulamento.Juridica import Juridica

p1 = Pessoa(1, 'kerol', 'rua amalia', '5555555')
p1.imprimeNome()
p1.getTelefone()
print()

p2 = Fisica('123456789', '30', 60, 1.50)
p2.imprimeCPF()
p2.GetIMC()
print()

p3 = Juridica('123456789101', 'Empresa_Exercício','20')
p3.imprimeCNPJ()
p3.GetNotaFiscal()
