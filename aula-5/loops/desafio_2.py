

for i in range(1,11):
    if  i % 2 == 0:
        continue
    else:
        print(i)
        
print("------")        
letras = ["a","b","c","d","e","f","g"]

for letra in letras:
    if letra in ["a", "e", "i", "o", "u"]:
        pass
    else:
        print(letra)