# 1. Variáveis e Strings (Gerador de E-mail Corporativo) Escreva um programa que peça
# ao usuário para digitar seu primeiro nome e, em seguida, seu sobrenome. O programa deve
# juntar os dois e criar um endereço de e-mail no formato
# nome.sobrenome@empresa.com.br.
# Dica: Lembre-se de que e-mails não possuem letras maiúsculas. Pesquise
# como usar o método .lower() para garantir que o e-mail final fique todo em
# letras minúsculas.

nome = str(input("digite aqui o seu nome "))
sobrenome = str(input("digite aqui o seu sobrenome "))

email_formatado = nome + sobrenome
print(email_formatado.lower() + "@empresa.com.br")