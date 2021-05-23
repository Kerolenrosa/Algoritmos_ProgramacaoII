from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
        self.fim = None
    
    def inserir(self, valor) :
        if self.inicio:
            aux = self.inicio
            while( aux.proximo ) :
                aux = aux.proximo
            
            aux.proximo = No(valor)
            aux.proximo.anterior = aux
            self.fim = aux.proximo
        else: 
            self.inicio = No(valor)
            self.fim = self.inicio
        self.tamanho += 1
        

    def imprimir(self): 
        if( self.inicio == None ) :
            print( "Lista Vazia!!")
        else:
            aux = self.inicio
            while ( aux  ) :      
                #Não estou conseguindo acessar o atributo "dado" do objeto anterior, apenas isso que ficou faltando                        
                print( 'Valor anterior: ', aux.anterior,  '------  Valor atual: ', aux.dado , "\n")
                aux = aux.proximo
            print("Tamanho da lista: ", self.tamanho)
            print("--------------------------")

    def imprimirInverso(self):
        
        if( self.inicio == None ) :
            print( "Lista Vazia!!")
        else:
            aux = self.fim
            while ( aux  ) :
                #Não estou conseguindo acessar o atributo "dado" do objeto anterior, apenas isso que ficou faltando
                print( 'Valor anterior: ', aux.anterior,  '------  Valor atual: ', aux.dado , "\n")
                aux = aux.anterior
            print("Tamanho da lista: ", self.tamanho)
            print("--------------------------")
