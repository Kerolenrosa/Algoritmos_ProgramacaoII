
class Pessoa():
    def __init__(self, id, nome, endereco, telefone):
        self.__id = id
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def imprimeNome(self):
        print('Nome cadastrado: ', self.nome)

    def __imprimeTelefone(self):
        print('Telefone cadastrado: ', self.__telefone)

    def getTelefone(self):
        self.__imprimeTelefone()