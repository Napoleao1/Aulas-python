# O que deve fazer: Peça ao utilizador para digitar um número inteiro positivo. Utilize um laço for

# em conjunto com a função range() para calcular a soma de todos os números pares desde 0
# até ao número inserido pelo utilizador (inclusive).
# Dica: A função range() pode receber 3 argumentos: início, fim e "salto" (range(0, numero+1, 2)).
# Exemplo Esperado:
# Digite um número: 6
# A soma dos pares é: 12 (pois 0 + 2 + 4 + 6 = 12)


numero = int(input("digite um numero positivo: "))

    
def soma_pares(numero):
    soma = 0
    for par in (range(0, numero+1, 2)):
        soma = soma + par
    return soma 
                 
    
print(soma_pares(numero))