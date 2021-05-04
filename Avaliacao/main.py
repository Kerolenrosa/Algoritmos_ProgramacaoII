from Computador import Computador
from Desktop import Desktop
from Notebook import Notebook
print()

print('--------------- Desktop ---------------')

D = Desktop('Lenovo', 'Branco', '2500', '650w')
print(D.getInformacoes)

print()

print('--------------- Notebook ---------------')
N = Notebook('Samsung', 'Prata', '7000', '700w')
print(N.getInformacoes)


