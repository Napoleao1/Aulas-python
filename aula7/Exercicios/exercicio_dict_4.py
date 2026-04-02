produtos = {
    "Computador": 5000.00,
    "Iphone 17": 7000.00,
    "Headset Gamer": 200.00,
    "Mouse Wireless": 100.00
}


produto = input("Escolha um produto para descobrir o preço: ").title()

print(f"O item que voce escolheu {produto} ele custa R${produtos[produto]}")