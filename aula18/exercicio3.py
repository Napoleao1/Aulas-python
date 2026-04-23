# 3. Contador de Vogais (Aulas 10 e 15)
# O que deve fazer: Crie uma função chamada contar_vogais(texto) que receba uma string. A
# função deve analisar a palavra e devolver a quantidade exata de vogais (a, e, i, o, u) que ela
# possui.

# Passo a passo sugerido:
# 1. Converta o texto recebido para letras minúsculas (método .lower()).
# 2. Crie uma variável total = 0.
# 3. Use um laço for para percorrer letra por letra da string.
# 4. Se a letra estiver na string "aeiou", aumente o total em 1.
# 5. Use o return para devolver o total.



def contar_vogais(texto):
    total = 0
    for letra in texto:
        if letra in "aeiou":
            total = total + 1
    return total
            
            
try:
    texto = str(input("digite um texto para contar as vogais: "))
    if texto == "":
        raise ValueError
    print(contar_vogais(texto))
except ValueError:
    print("voce nao digitou nada")


            
            

                