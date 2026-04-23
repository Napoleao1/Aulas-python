# 6. Sistema de Descontos (Aulas 15 e 16)
# O que deve fazer: Crie uma função chamada calcular_preco(valor, desconto=0.1). Repare que
# o desconto é um parâmetro opcional que, por defeito, vale 10% (0.1).
# Exemplos de Chamadas e Retornos:
# ● Se chamar calcular_preco(100), a função devolve 90.0 (porque aplicou o desconto padrão
# de 10%).
# ● Se chamar calcular_preco(100, 0.5), a função devolve 50.0 (porque substituiu o 10% por
# 50%).


def calcular_preco(valor, desconto =0.1):
    preco_final = valor -  (valor * desconto)
    
    return preco_final   
    
    
print(calcular_preco(500, 0.40))