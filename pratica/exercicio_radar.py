# Desafio 1 Radar de Velocidade
# Escreva um programa que pergunte a velocidade do carro. SE for maior que 80 km/h, exiba uma mensagem
# dizendo que ele foi multado. SENÃO, exiba uma mensagem de "Boa viagem! Dirija com segurança."



velocidade = int(input("qual a velocidade do carro? "))
if velocidade > 80:
    print("Voce foi multado")
else:
    print("Boa viagem! Dirija com segurança.")
    
    