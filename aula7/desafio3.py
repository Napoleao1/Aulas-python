# Desafio 3 A Lista de Produtos
# 1. Crie uma lista estoque. Dentro dela, coloque 3 dicionários representando produtos (chaves "produto" e
# "preco").
# 2. Use um laço for para percorrer a lista.
# 3. A cada volta, imprima apenas o nome de cada produto.


estoque = [
    {"produto": "Tênis Nike", "preco": 399.00},
    {"produto": "Camiseta Básica", "preco": 100.00},
    {"produto": "Calça Baggy", "preco": 312.00}
]


for item in estoque:
    print(item["produto"])