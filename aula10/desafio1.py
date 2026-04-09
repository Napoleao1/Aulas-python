 # criar funcao converter o dolar que recebe valor_dolar e taxa_cambio
 #deve calcular o valor em reais
 
# usar o return para devolver o valor
#chamar a funcao guardar em uma variavel e imprimir


def converter_dolar(valor_dolar, taxa_cambio):
    valor_reais = valor_dolar * taxa_cambio
    
    return valor_reais

conversao = converter_dolar(100, 5.10)

print(f"o valor em reais é R${conversao:.2f}")



def converter_reais(valor_reais, taxa_cambio):
    valor_dolar = valor_reais / taxa_cambio
    return valor_dolar


conversao_2 = converter_reais(510, 5.10)
print(f"o valor em dolares é R${conversao_2:.2f}")
