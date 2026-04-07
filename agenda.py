import time
import os


agenda = []

while True:
    os.system("cls")
    
    print("Menu de opcões da agenda")
    print("1 • Adicionar contato a agenda")
    print("2 • Ver Lista de contatos ")
    print("3 • Excluir contato ")
    print("4 • Apagar agenda")
    print("5 • Sair ")
    escolha = int(input("Escolha uma opção para acessar a agenda: "))

    if escolha == 1:
        nome_contato = input("digite o nome do contato: ")
        numero_contato = input("digite o numero do contato: ")
        email_contato = input("digite o e-mail do contato: ")

        novo_contato = {
            "nome": nome_contato,
            "telefone": numero_contato,
            "email": email_contato
            }
        
        for contato in agenda:
            if contato["nome"] == nome_contato:
                print("este nome ja existe na agenda")
                break
        else:
            agenda.append(novo_contato)
            print(" contato adicionado com sucesso a sua agenda")
            time.sleep(2)
        
    elif escolha == 2:
        
        if len(agenda) == 0:
            print("A lista de contatos esta vazia")
            continue
        print(f"voce tem {len(agenda)} contatos salvo na agenda")
        
        for contato in agenda:
            print(f"nome: {contato["nome"]} ---- telefone: {contato["telefone"]} ---- email:{contato["email"]}")
        time.sleep(5)

        
    elif escolha == 3:
        deletar_numero = input("digite o nome para deletar")
        for contato in agenda:
            if contato["nome"] == deletar_numero:
                agenda.remove(contato)
                break
            
    elif escolha == 4:
        deletar_agenda = input("digite 4 para deletar a agenda")
        agenda = []
        deletar_agenda = agenda
        print =(f"sua agenda esta vazia {agenda}")
               
                                
    elif escolha == 5:
        print("Voce saiu da agenda....")
        time.sleep(3)
        
        break
    
    else:
        print("escolha uma opcao valida")
        time.sleep(3)


