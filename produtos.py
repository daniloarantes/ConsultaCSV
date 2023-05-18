import os.path
import datetime

arquivo = "produtos.csv"

if (os.path.isfile(arquivo)):
    produtos = open(arquivo, 'r', encoding='UTF-8')
    tamanho = os.path.getsize(arquivo)
    modificacao = os.path.getmtime(arquivo)
    print("Data de Modificação:", datetime.datetime.fromtimestamp(modificacao))
    print("Tamanho:", tamanho)

    listaProdutos = []

    for linha in produtos:
        colunas = linha.strip().split(';')
        colunas[0] = int(colunas[0])
        colunas[2] = int(colunas[2])
        colunas[3] = float(colunas[3])
        listaProdutos.append(colunas)
    
    produtos.close()

for prod in listaProdutos:
    print("Código:",prod[0])
    print("Descrição:", prod[1])
    print("Quantidade:", prod[2])
    print("Preço:", prod[3])
    print(f"Total: R${prod[2]*prod[3]:.2f}")
    print("")


    

