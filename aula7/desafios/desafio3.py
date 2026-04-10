# ano = int(input("Digite um ano para verificar se ele é bissexto ou ano normal: "))
# if (ano % 4 == 0 and ano % 100 != 0) or  (ano % 400 == 0):
#     print("ano é bissexto")
# else:
#     print("ano é normal")
    

while True:
    try:
        ano = int(input("Digite um ano para verificar se ele é bissexto ou ano normal: "))

        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"O ano {ano} é bissexto!")
            break 
        else:
            print(f"O ano {ano} é um ano normal.")
            
    except ValueError:
        print("Opção inválida! Por favor, digite um número (ex: 2024).")