# Desafio 3 A Calculadora Dupla
# 1. Crie uma função calcular_dobro_e_triplo que recebe um numero.
# 2. Calcule o dobro e o triplo desse número.
# 3. Use o return para devolver os dois valores ao mesmo tempo.


def calcular_dobro_e_triplo(numero):
    dobro = numero * 2
    triplo = numero * 3
    return dobro, triplo


valor_dobro, valor_triplo = calcular_dobro_e_triplo(10)

print(valor_dobro, valor_triplo)