peso = float(input("Digite o seu peso em KG: "))
altura = float(input("Digite a sua altura em metros: "))

imc = round(peso / (altura * altura), 2)

if imc < 18.5:
    print(f"você está abaixo do peso com imc de {imc}")
    
elif imc >= 18.5 and imc <= 24.9:
    print(f"Peso normal, você está muito bem imc de {imc}")
    
elif imc >= 25 and imc <= 29.9:
    print(f"Você está com excesso de peso imc de {imc}")
    
else:
    print(f"Você está com obesidade imc de {imc}")
    