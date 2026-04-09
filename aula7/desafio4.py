# Desafio 4 O Buscador de Pessoas
# 1. Crie uma lista clientes com 3 dicionários (chaves "nome" e "cidade").
# 2. Peça pro usuário digitar o nome de uma cidade via input().
# 3. Percorra a lista com for e crie um if: SE a cidade do dicionário for igual à digitada, imprima o nome do
# cliente!


carteira_clientes = [
        {"nome": "Lucas", "cidade": "Sao paulo"},
        {"nome": "Joao", "cidade": "Rio de janeiro"},
        {"nome": "Jose", "cidade": "Porto Alegre"}
        ]
    
cidade_escolhida = input("digite o nome de uma cidade: ")


for cliente in carteira_clientes:
    if cliente["cidade"].lower() == cidade_escolhida.lower():
        print(f"Cliente encontrado: {cliente['nome']}")