# Desafio 2 Classificador de Idades
# Peça a idade do usuário. Usando if, elif e else:
# - Menor que 13 anos: imprima "Criança".
# - Entre 13 e 17 (inclusive): imprima "Adolescente" Dica: use o 'and').
# - Entre 18 e 59 (inclusive): imprima "Adulto".
# - 60 ou maior: imprima "Idoso".



idade = int(input("digite aqui a sua idade "))

if idade <= 13:
    print("Criança")
    
elif idade > 13 and idade <= 17:
    print("Adolescente")

elif idade >= 18 and idade <= 59:
    print("Adulto")

else:
    print("idoso")