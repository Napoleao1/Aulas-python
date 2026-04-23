#     Nível Fácil (Foco em sintaxe e estruturas básicas)


# 1. Classificador de Clima e Temperatura (Aulas 02, 03 e 04)
# O que deve fazer: Crie um script que receba uma temperatura em graus Celsius (float)
# inserida pelo utilizador. Calcule a conversão para Fahrenheit através da fórmula F = (C * 1.8) +
# 32. De seguida, utilize estruturas if/elif/else para classificar o clima.
# Regras de Classificação:
# ● Menor que 15°C: "Frio"
# ● Entre 15°C e 25°C: "Agradável"
# ● Maior que 25°C: "Quente"
# Exemplo Esperado:
# Digite a temperatura em Celsius: 20
# Resultado: 20.0°C equivalem a 68.0°F. O clima está Agradável.

c = float(input("digite a temperatura em graus celcius: °C: "))

F = (c * 1.8 ) + 32

if c < 15:
    print(F"Resultado: {c}°C equivalem a {F}°F O clima está frio")
elif c >= 15 and c <= 25:
    print(f"Resultado: {c}°C equivalem a {F}°F O clima está Agradavel")
else:
    print(F"Resultado: {c}°C equivalem a {F}°F O clima está Quente")
    
    