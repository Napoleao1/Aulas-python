# Desafio 1: O Matemático (import)
# 1. Importe a biblioteca math no topo do arquivo.
# 2. Peça ao usuário para digitar um número com casas decimais via input.
# 3. Use a função math.ceil() (teto) para arredondar o número PARA CIMA e math.floor() (chão) para
# arredondar PARA BAIXO e imprima-os.



import math 

numero = float(input("digite um numero com casas decimais: "))

teto = math.ceil(numero)
chao = math.floor(numero)
print(f"o numero é arrendonda para cima é {teto}, e o numero arredondado para baixo é {chao}")