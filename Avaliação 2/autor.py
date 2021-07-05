class autor ():

    def __init__(self, id, nome):

        self._id = id
        self.nome = nome

    
    def imprimir(self):

        print("ID", self._id, "NOME", self.nome)
