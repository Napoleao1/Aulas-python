cardapio = {
    "pizza": 25.00,
    "hamburguer": 18.00,
    "cachorro-quente": 10.00,
    "Xis": 20.00
}


for produto, preço in cardapio.items():
    print(F"  Produto: {produto} | Preço: R$ {preço}")