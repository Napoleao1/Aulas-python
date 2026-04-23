# Exercício 7: Gerenciador de Estoque
# Módulos aplicados: Aulas 12, 13 e 14.
# Crie um dicionário para simular um estoque de loja, onde a chave é o nome do produto e o
# valor é a quantidade (ex: {'teclado': 10, 'mouse': 5}).

# 1. Crie um loop que pergunte ao usuário: “Qual produto deseja vender?” e “Quantas unida-
# des?”.

# 2. Verifique se o produto existe no dicionário. Se não existir, exiba “Produto não cadastrado”.
# 3. Se existir, verifique se há quantidade suficiente. Se houver, subtraia o valor do estoque e
# exiba a venda confirmada. Se não houver, exiba “Estoque insuficiente”.
# 4. Digitar ”sair” deve encerrar o programa.
# 5. No final, use um laço for com .items() para imprimir o estoque final atualizado.

estoque = {
    'teclado': 10,
    'mouse': 5,
    'monitor': 12
}


while True:
produto =  input("Qual produto desenha vender e quantas unidades")