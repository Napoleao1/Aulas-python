import random

pc = random.choice(["Pedra", "Papel", "Tesoura"])
pc = pc.lower()

jogador = str(input("escolha uma opção entre Pedra Papel e Tesoura: "))
jogador = jogador.lower()
if jogador == pc:
    print(" empate, a maquina escolheu", pc)

elif (jogador == "pedra" and pc == "tesoura") or (jogador == "papel" and pc == "pedra") or (jogador == "tesoura" and pc == "papel"):
    print("Você ganhou da maquina ela escolheu", pc)
elif jogador not in ["pedra", "papel", "tesoura"]:
    print("opção invalida, jogador entre pedra, papel ou tesoura")  
else:
    print(f"voce perdeu para a maquina ela escolheu {pc}")