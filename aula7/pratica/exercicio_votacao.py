# Desafio 2 Pode votar? Relacional)
# Peça o ano de nascimento. Calcule a idade exata. Em seguida, crie uma variável chamada pode_votar que
# guardará a verificação: idade >= 16. Imprima o resultado da variável True ou False).

ano_nascimento = int(input("digite aqui o ano que voce nasceu: "))

idade = 2026 - ano_nascimento

pode_votar = idade >= 16
print(pode_votar)