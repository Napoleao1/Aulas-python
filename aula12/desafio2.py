# Desafio 2: O Segurança da Balada (in)
# 1. Crie a lista: lista_vip = ["Marcos", "Julia", "Roberto"].
# 2. Peça o nome do usuário usando o input(). Use o método .title() no input para padronizar a primeira letra
# maiúscula!
# 3. Use o operador in. Se estiver na lista, "Pode entrar!". Senão, "Você não está na lista.".


lista_vip = ["Marcos", "Julia", "Roberto"]

nome_user = str(input("Digite um nome do usuario ")).title()


if nome_user in lista_vip:
    print("pode entrar")
    
else:
    print("acesso negado")