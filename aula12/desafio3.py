# Desafio 3: O Menu Elegante (match case)
# 1. Crie um while True: que exibe um menu: [1] Pizza [2] Hambúrguer [0] Sair.
# 2. Peça a opção do usuário.
# 3. Use o match case para avaliar a resposta. Caso 0, imprima "Saindo..." e use o break! Caso _, imprima "Opção
# inválida".



while True:
    opcao = input("1- Pizza\n2- Hamburguer\n0- Sair: ")
    
    match opcao:
        case "0":
            print("voce saiu do programa ")
            break
        case "1":
            print("voce escolheu pizza")
        case "2":
            print("voce escolheu hamburguer")
        case _:
            print("opcao invalida")
        