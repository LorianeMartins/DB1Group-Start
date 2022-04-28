"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. """

produto_1 = float(input("Informe o preço do produto 1 em R$: "))
produto_2 = float(input("Informe o preço do produto 2 em R$ : "))
produto_3 = float(input("Informe o preço do produto 3 em R$: "))

produtos = []

produtos.append(produto_1)
produtos.append(produto_2)
produtos.append(produto_3)

menor_preco = min(produtos)
index_menor_preco = produtos.index(menor_preco)

print(f"\nO produto com menor preço é o {index_menor_preco + 1} : R${menor_preco}")