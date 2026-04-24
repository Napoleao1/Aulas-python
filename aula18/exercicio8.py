# 9. Jogo de Par ou Ímpar (Aulas 06 e 19)
# O que deve fazer: Simular o clássico jogo. Importe a biblioteca random.

# Num loop while, pergunte se o utilizador quer "Par" ou "Impar". Peça para digitar um número (0
# a 10). O computador deve sortear o seu próprio número (random.randint(0, 10)).

# Lógica: Some os dois números. Se soma % 2 == 0, o resultado é par. Caso contrário, é ímpar.
# Verifique se o resultado corresponde à escolha inicial do utilizador e declare o vencedor.
# Pergunte se quer jogar novamente antes de continuar o loop.


import random

while True:
    escolha = input("voce quer Par ou Impar? ").lower()
    try:
        numero = int(input("digite um numero de 0 a 10: "))
    except ValueError:
        print("digite um numero")
        continue
    numero_sorteado = (random.randint(0, 10))
    total = numero + numero_sorteado

    if total % 2 == 0:
        if escolha == "par":
            print("O jogador venceu")
        else:
            print("O jgoador perdeu")
    else:
        if escolha == "impar":
            print("venceu")
        else:
            print("perdeu")

    jogar = input("Quer jogar de novo? (s/n): ").lower()
    if jogar == "n":
        break
