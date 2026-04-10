# Desafio 1 O Conversor Seguro
# 1. Crie uma variável preco que pede o valor de um produto (usando input para float).
# 2. Envolva isso num bloco try/except.
# 3. Se o usuário digitar texto, capture o ValueError e imprima: "Por favor, digite usando apenas números e
# pontos.".
# 4. Teste o programa errando de propósito.

# Desafio 2 Calculadora à Prova de Falhas
# 1. Peça ao usuário 2 números inteiros (num1 e num2.
# 2. Crie um bloco try que tenta imprimir o resultado de num1 / num2.
# 3. Crie um except ZeroDivisionError que imprima: "Não é possível dividir por zero!".
# 4. Teste digitando 0 para o divisor.

# try: 
#     preco = float(input("Qual o valor do produto"))

# except ValueError:
#     print("Por favor, digite usando apenas números e pontos")
    
    
    
# print("digite dois numero inteiros")

# try:
#    num1 = int(input("digite o numero 1: "))
#    num2 = int(input("digite o numero 2: "))

#     resultado = num1 / num2
#     print(f"o resultado é {resultado}")
# except ZeroDivisionError:
#      print("Não é possível dividir por zero!")
     
     
     
# Desafio 3 O Loop Blindado
# 1. Crie um ciclo while True:.
# 2. Peça o ano de nascimento (int).
# 3. Use try/except ValueError. Se ele digitar letras, avise o erro e deixe o while repetir a pergunta
# infinitamente.
# 4. Se digitar corretamente, use o break para sair e imprima o sucesso.

# Desafio 4 O Acesso Proibido
# 1. Crie a lista: cores = ["Azul", "Verde", "Amarelo"].
# 2. Peça a posição da cor 0, 1 ou 2) via int(input()).
# 3. Num try, imprima a cor escolhida: print(cores[numero_digitado]).
# 4. Capture o erro usando except IndexError: e imprima "Posição inexistente!" se ele digitar 5.


while True:
    try:
        ano_nasc = int(input("digite o ano que voce nasceu: "))
        if ano_nasc < 0:
            raise ValueError
        print(f"seu ano é {ano_nasc}")
        break
    except ValueError:
        print("voce digitou letras, digite um numero valido")


try:
    cores = ["Azul", "Verde", "Amarelo"]
    posicao = int(input("Digite a posicao correta da cor escolhida: "))
    print(cores[posicao])
except IndexError:
    print("Posição Inexistente")
