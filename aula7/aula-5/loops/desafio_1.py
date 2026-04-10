# Desafio 1 O Somador Infinito
# Crie uma variável soma = 0 e um laço while True:. Dentro dele, peça ao usuário um número inteiro. SE o
# número for 0, use o break. SENÃO, adicione o número à variável soma. No final, imprima o resultado total
# da soma na tela.



soma = 0

while True:
    numero = int(input("digite um numero inteiro: "))
    
    if numero == 0:
        break
    
    soma += numero

print(f"o total é, {soma}")