import time
import os


agenda = []

while True:
    os.system("cls")
    
    print("Menu de opcões da agenda")
    print("1 • Adicionar contato a agenda")
    print("2 • Ver Lista de contatos ")
    print("3 • Excluir contato ")
    print("4 • Sair")
    escolha = int(input("Escolha uma opção para acessar a agenda: "))

    if escolha == 1:
        nome_contato = input("digite o nome do contato: ")
        numero_contato = input("digite o numero do contato: ")

        novo_contato = {
            "nome": nome_contato,
            "telefone": numero_contato
            }
        agenda.append(novo_contato)
        print(" contato adicionado com sucesso a sua agenda")
        time.sleep(2)
        
    elif escolha == 2:
        print(agenda)
        time.sleep(5)

        
    elif escolha == 3:
        deletar_numero = input("digite o nome para deletar")
        for contato in agenda:
            if contato["nome"] == deletar_numero:
                agenda.remove(contato)
                break
                                
    elif escolha == 4:
        print("Voce saiu da agenda....")
        time.sleep(3)
        
        break
    
    else:
        print("escolha uma opcao valida")
        time.sleep(3)
