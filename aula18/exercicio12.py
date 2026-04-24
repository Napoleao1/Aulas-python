# 12. O Separador de Tipos (Aulas 10 e 19)

# O que deve fazer: Dada a lista misturada: dados = [10, "Python", True, 3.14, "Código", 42, False],

# crie quatro listas vazias (uma para inteiros, uma para floats, uma para strings e uma para
# booleanos).
# Faça um laço for que passe por cada elemento da lista principal. 
# Utilize a função type() e if/elif
# para descobrir o tipo do dado e usar o .append() na lista correta. No final, imprima as quatro
# listas separadas.

dados = [10, "Python", True, 3.14, "Código", 42, False]


lista_string = []
lista_float = []
lista_int = []
lista_bool = []

def atualizar_listas():
    for dado in dados:
        if type(dado) == str:
            lista_string.append(dado)
        elif type(dado) == float:
            lista_float.append(dado)
        elif type(dado) == int:
            lista_int.append(dado)
        elif type(dado) == bool:
            lista_bool.append(dado)
    return lista_string, lista_float, lista_int, lista_bool



print(atualizar_listas())
    