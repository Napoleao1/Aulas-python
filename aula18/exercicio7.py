# Estatísticas Numéricas (Aulas 06, 10 e 11)
# O que deve fazer: Crie uma lista vazia. Crie um loop infinito (while True) que pede

# repetidamente um número inteiro ao utilizador e o adiciona à lista.
# Condição de paragem: O loop deve ser interrompido (break) assim que o utilizador digitar o
# número 0. O número zero não deve ser inserido na lista.
# Ao final, utilize as funções nativas max(), min() e sum() para imprimir o maior valor digitado, o
# menor e a soma total de todos os elementos.


lista = []

numero = 0

while True:
    numero = int(input("digite um numero: "))
    if numero == 0:
        break
    else:
        lista.append(numero)
    
print(max(lista))
print(min(lista))
print(sum(lista))