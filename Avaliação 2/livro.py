class livro ():

    def __init__(self, id, titulo, autor):

        self.id = id
        self.titulo = titulo
        self.autor = autor
        

    def imprimir(self):

        print ("ID", self.id, "TITULO", self.titulo, "AUTOR", self.autor.nome)