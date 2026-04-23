# 4. Empacotador de Tuplas (Aula 11)
# O que deve fazer: Crie uma lista vazia. Peça ao utilizador para digitar 3 nomes de cidades
# consecutivas, usando o método .append() para inseri-las na lista. Em seguida, converta essa
# lista numa tupla através da função nativa tuple().
# Por fim, crie três variáveis (cidade1, cidade2, cidade3 = tupla_criada) para desempacotar e
# imprimi-las separadamente no terminal.


lista = []
    
    
def pedir_cidade():
    for i in range(3):
        cidade = input("digite um nome deu uma cidade: ")
        lista.append(cidade)
        
pedir_cidade()
tupla = tuple(lista)   

cidade1, cidade2, cidade3 = tupla

print(cidade1)
print(cidade2)
print(cidade3)