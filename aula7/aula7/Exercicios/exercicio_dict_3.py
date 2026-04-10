# Desafio 3 Limpeza de Dados
# Ainda usando o dicionário perfil do desafio anterior:
# 1. O usuário decidiu ocultar o e-mail. Use o método .pop() para deletar a chave "email" do dicionário de
# forma segura.
# 2. Imprima o dicionário para confirmar que o e-mail desapareceu.

# Desafio 4 O Estoque da Loja
# 1. Crie um dicionário produtos onde as chaves são os nomes dos produtos e os valores são os preços
# numéricos. Ex: {"Notebook": 3500.00, "Mouse": 150.00.
# 2. Peça ao usuário através de input() o nome de um produto.
# 3. Acesse o dicionário e imprima na tela o preço do produto que o usuário digitou.





info = {
    "nome": "ernani",
    "idade": "25",
    "email": "ernaninandoxd@gmail.com"   
}


info.pop("email")

print(info)


