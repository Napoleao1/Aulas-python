# O Fatiador de Nomes (Aulas 02, 10 e 11)

# O que deve fazer: Peça ao utilizador o seu nome completo (ex: "Ana Carolina Santos").
# 1. Use a função nome.split() para criar uma lista com as palavras do nome: ["Ana", "Carolina",
# "Santos"].
# 2. Imprima o primeiro nome acessando o índice [0].
# 3. Imprima o último nome acessando o índice [-1] (funciona para qualquer tamanho de
# nome).
# 4. Imprima as iniciais de uma forma elegante, como a primeira letra do primeiro nome
# seguida do apelido: "A. Santos".


def nome_completo():
    nome = input("digite seu nome completo: ").split()
    print(nome[0])
    print(nome[-1])
    print(f"{nome[0][1]}, {nome[-1]}")


teste = nome_completo()
