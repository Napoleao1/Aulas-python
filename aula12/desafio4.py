# Desafio 4: O Relógio do Sistema (datetime)
# 1. Importe a biblioteca datetime e crie uma função saudacao_hora().
# 2. Dentro dela, pegue a hora atual com hora_atual = datetime.datetime.now().hour.
# 3. Faça um if/elif: se a hora for menor que 12, retorne "Bom dia!". Se for menor que 18, retorne "Boa tarde!".
# Senão, "Boa noite!". Chame a função.

import datetime

def saudacao_hora():
    hora_atual = datetime.datetime.now().hour
    return hora_atual


hour_now = saudacao_hora()


if hour_now < 12:
    print("bom dia")
    
elif hour_now < 18:
    print("Boa tarde")
    
else:
    print("boa noite")
    
    
print(f"hora atual: {hour_now} ")

