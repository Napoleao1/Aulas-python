saldo = 1000

print(" opcão - 1 ver saldo \n opcao - 2 saque \n opcao - 3 Sair")
opcao = float(input("escolha uma opcao para continuar: "))

if opcao == 1:

    print("seu saldo é", saldo)
    
elif opcao == 2:
    valor = float(input("Digite o valor que quer sacar: "))
    
    if valor <= saldo:
        saldo = saldo - valor
        print(f"seu saque foi de {valor} e o seu saldo restante é {saldo}")
    else:
        print("Saldo insuficiente")
    
elif opcao == 3:
    print("Obrigado, volte sempre")

else:
    print("opcao invalida")