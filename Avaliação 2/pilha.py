from No import No

class pilha:

    def __init__(self):
        self.topo = None
        self.tamanho = 0


    def inserir(self,valor):
        no = No (valor)
        no.proximo = self.topo
        self.topo = no
        self.tamanho+= 1


    def remover(self):
        if self.tamanho > 0:
            no = self.topo
            self.topo = self.topo.proximo
            self.tamanho -= 1


    def top(self):
        if self.tamanho > 0:
            print (self.topo.dado )


    def imprimir(self):
        topo = self.topo

        while (topo):
            str(topo.dado.imprimir())
            topo = topo.proximo