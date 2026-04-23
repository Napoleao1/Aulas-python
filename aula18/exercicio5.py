# 5. Tratamento de Erro Simples (Aulas 15 e 17)
# O que deve fazer: Crie uma função dobrar_numero(). Dentro dela, use input() para pedir um
# número.
# O desafio: Se o utilizador escrever a palavra "Dez" em vez do número 10, o Python vai gerar um
# erro chamado ValueError ao tentar converter para float. O seu código não deve apresentar
# aquele texto vermelho assustador no terminal. Deve usar um bloco try/except ValueError: para
# capturar este problema e imprimir uma mensagem amigável: "Por favor, digite apenas
# números!".


def dobrar_numero():
    try:
        numero = float(input("digite um numero: "))
        return numero * 2
    except ValueError:
        print("Por favor, digite apenas números!")


print(dobrar_numero())

