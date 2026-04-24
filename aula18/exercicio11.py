# Gerador de Senhas (Aulas 07 e 19)
# O que deve fazer: Importe as bibliotecas random e string. Crie uma função que peça a
# quantidade de caracteres para uma senha.

# Dica de ouro: A variável string.ascii_letters + string.digits contém todas as letras e números
# possíveis.

# Faça um laço for rodar a quantidade de vezes pedida e, em cada volta, sorteie um caractere
# com random.choice(), concatenando numa variável senha_final. A função deve devolver essa
# senha gerada.


import random, string 

def qntd_letras():
    pedir = int(input("informe quantos caracteres voce quer na sua senha: "))
    senha_final = ""
    for i in range(pedir):
        letras_sorteadas = random.choice(string.ascii_letters + string.digits)
        senha_final += letras_sorteadas
    return senha_final
print(qntd_letras())