# Crie controlador.py. Importe from modelo import inserir_produto_bd. Crie validar_produto(nome, preco)
# verificando se o nome está vazio. Se tudo estiver correto, converta o preço para float, chame a função do
# banco e retorne True.

from models.modelo import inserir_produto_bd


def validar_produto(nome, preco):
    if nome == "":
        return False
    
    preco = float(preco)
    inserir_produto_bd(nome, preco)
    return True
        