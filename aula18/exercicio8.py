# 9. Jogo de Par ou Ímpar (Aulas 06 e 19)
# O que deve fazer: Simular o clássico jogo. Importe a biblioteca random.

# Num loop while, pergunte se o utilizador quer "Par" ou "Impar". Peça para digitar um número (0
# a 10). O computador deve sortear o seu próprio número (random.randint(0, 10)).

# Lógica: Some os dois números. Se soma % 2 == 0, o resultado é par. Caso contrário, é ímpar.
# Verifique se o resultado corresponde à escolha inicial do utilizador e declare o vencedor.
# Pergunte se quer jogar novamente antes de continuar o loop.


import random

while True:
    print("voce quer Par ou Impar? ")
    numero = int(input("digite um numero de 0 a 10"))
    numero_sorteado = (random.randint(0, 10))
    total = numero + numero_sorteado
    
    if numero_sorteado % 2 == 0:
        print("par")
    else:
        print("impar")
    
    