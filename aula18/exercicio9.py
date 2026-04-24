# Dicionário de Sinônimos (Aulas 12 e 13)
# O que deve fazer: Crie um dicionário base no código, ex: dicionario = {"feliz": ["alegre",
# "contente"], "rápido": ["veloz"]}.
# Peça ao utilizador uma palavra.

# ● Se ela existir no dicionário (use if palavra in dicionario:), imprima a lista de sinônimos.
# ● Se não existir, pergunte-lhe: "Não conheço esta palavra. Diga-me um sinônimo para ela?".
# Adicione a nova palavra e o seu sinônimo (dentro de uma lista) ao dicionário, imprimindo o
# dicionário atualizado no fim.



dicionario = {"feliz": ["alegre", "contete"], "rapido": ["veloz"]}

palavra = input("digite uma palavra: ")
if palavra in dicionario:
    print(dicionario[palavra])
else:
    palavra_2 = input("nao conheco essa palavra, me diz um sinonimo para ela: ")
    dicionario[palavra] = [palavra_2]
print(dicionario)