# 2. Operadores Matemáticos (Calculadora de IMC) Crie um programa que calcule o Índice
# de Massa Corporal (IMC) do usuário. O programa deve pedir o peso (em kg) e a altura (em
# metros). A fórmula do IMC é o peso dividido pela altura ao quadrado. Imprima o valor do
# IMC na tela.
# Dica: Para elevar um número ao quadrado em Python, você pode usar o
# operador de exponenciação (**) ou simplesmente multiplicar a altura por ela
# mesma. Cuidado com o tipo de dado da altura, use float().


peso = int(input("digite aqui o seu peso em kg: ")) 
altura = float(input("digite aqui a sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc}")