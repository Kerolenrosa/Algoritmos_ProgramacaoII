
from autor import autor
from livro import livro
from pilha import pilha

autor1 = autor (1, "Steve")
autor2 = autor (2, "Clarisse")
autor3 = autor (3, "Carlos")

livro1 = livro (1, "O Poder do Hábito", autor2)
livro2 = livro (2, "A Garota do Lago", autor1)
livro3 = livro (3, "Mulheres que correm com os lobos", autor3)
livro4 = livro (4, "O Homem mais rico da BabilÔnia", autor2)

pilha = pilha()

pilha.inserir (livro1)

pilha.inserir (livro2)

pilha.inserir (livro3)

pilha.imprimir()
print()

pilha.remover()

pilha.imprimir()
print()

pilha.inserir (livro4)

pilha.imprimir()
print()

pilha.remover()

pilha.imprimir()
print()
