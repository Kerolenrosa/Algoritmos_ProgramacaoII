from Torre import Torre
from Apartamento import Apartamento
from Fila import Fila


t1 = Torre()
t1.cadastrar(1, "Copacabana", "Bloco A")
t1.imprimir ()

print()

a1 = Apartamento ()
a1.cadastrar(10, 405, 24, t1)
a1.imprimir ()

fila = Fila()

fila.adicionar(a1)
fila.imprimir()

print()

a2 = Apartamento ()
a2.cadastrar(20, 805, 50, t1)

fila.adicionar(a2)
fila.imprimir()

fila.remover()
fila.imprimir()
