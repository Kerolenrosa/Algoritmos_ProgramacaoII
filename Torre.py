class Torre ():

    def __init__(self, id = 0, nome = None, endereco = None):

        self.id = id
        self.nome = nome
        self.endereco = endereco

    def cadastrar (self, id, nome, endereco): 
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def imprimir (self):
        print ("A torre possui id", self.id, "com o nome", self.nome, "e possui o endereço", self.endereco)
