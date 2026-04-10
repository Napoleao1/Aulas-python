# Desafio 2 O Verificador de Maioridade
# 1. Crie uma função eh_maior_de_idade que recebe uma idade.
# 2. Se a idade for >= 18, retorne True. Senão, retorne False.
# 3. No código global, crie um if que chame a função. Ex: if eh_maior_de_idade(20): print("Pode entrar!").


def eh_maior_de_idade(idade):
    if idade >= 18:
        return True
    else:
        return False
    

if eh_maior_de_idade(20):
    print("Pode entrar!")

else:
    print("acesso negado")