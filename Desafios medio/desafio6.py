# Exercício 6: O Jogo da Forca Simplificado
# Módulos aplicados: Aulas 06, 07, 10 e 19.
# Crie uma versão simplificada do jogo da forca.
# 1. Defina uma variável com a palavra secreta (ex: palavra = "python").
# 2. Crie uma lista vazia chamada letras_descobertas.


# 3. Dê ao usuário 5 tentativas. Use um while para controlar o jogo.
# 4. A cada rodada, exiba a palavra ocultando as letras não descobertas com ” _ ” (use um for
# na palavra secreta junto com o operador in na lista de letras descobertas).
# 5. Peça uma letra. Se a letra estiver na palavra secreta, adicione-a à lista letras_descobertas.
# Se não estiver, diminua 1 tentativa.
# 6. O jogo acaba se ele descobrir todas as letras (vitória) ou as tentativas chegarem a zero
# (derrota).


def verificar_vitoria(palavra, letras_descobertas):
    for letra in palavra:
        if letra not in letras_descobertas:
            return False
    return True


def exibir_palavra(palavra, letras_descobertas):
    for letra in palavra:
        if letra in letras_descobertas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()


def pedir_letra(palavra, letras_descobertas, tentativas):
    escolha = input("digite uma letra: ")
    if escolha in palavra:
        letras_descobertas.append(escolha)
    else:
        tentativas = tentativas - 1
        if tentativas == 0:
            print("voce perdeu mane")
    return tentativas


def jogar():
    palavra_secreta = "skateboard"
    letras_descobertas = []
    tentativas = 5

    while tentativas:
        if verificar_vitoria(palavra_secreta, letras_descobertas):
            print("voce ganhou")
            break
        exibir_palavra(palavra_secreta, letras_descobertas)
        tentativas = pedir_letra(palavra_secreta, letras_descobertas, tentativas)


jogar()

