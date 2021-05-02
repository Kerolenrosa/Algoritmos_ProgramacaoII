lst_produto = []
lst_preco_prod = []
lst_qtd_prod = []


def cadastrar_produto():
    produto = input("Informe o nome do produto: ").upper()
    preco = input("Informe o preço do produto: ")
    qtd = input("Informe a quantidade do produto: ")

    validar_produto(produto, preco, qtd)

    lst_produto.append(produto)
    lst_preco_prod.append(preco)
    lst_qtd_prod.append(qtd)


def validar_produto(produto, preco, qtd):
    while True:
        if produto == "":
            produto = input("Informe o nome do produto: ").upper()
        else:
            break

    while True:
        if preco == "":
            preco = input("Informe o preço do produto: ").upper()
        else:
            break

    while True:
        if qtd == "":
            qtd = input("Informe a quantidade do produto: ").upper()
        else:
            break

def listar_produto():
    print('Produto cadastrados')
    print()
    for indice, produto in enumerate(lst_produto):
        print(f"..{indice + 1} - Produto: {produto} .. Preço: {lst_preco_prod[indice]} .. Quantidade: {lst_qtd_prod[indice]}")



def retirar_produto():
    for indice, produto in enumerate(lst_produto):

        print(f"..{indice + 1} - Produto: {produto}")

    print()
    opcao = int(input('Informe o número do produto que deseja retirar: '))


    lst_produto.pop(opcao - 1)
    lst_preco_prod.pop(opcao - 1)
    lst_qtd_prod.pop(opcao - 1)



    print()
    print('Produto retirado da lista com sucesso.')


while True:
    escolha = input(''')
        Menu
        0-	Finalizar o programa
        1-	Cadastrar produto
        2-	Listar produtos
        3-  Retirar produto         
        Escolha:''')

    print()

    if escolha == '0':
        break
    elif escolha == '1':
        cadastrar_produto()

    elif escolha == '2':
        listar_produto()

    elif escolha == '3':
        retirar_produto()






