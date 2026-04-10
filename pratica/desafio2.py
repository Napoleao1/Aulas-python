# Desafio 2 A Média da Turma
# 1. Crie o dicionário de notas: notas = {"Matemática": 8.0, "História": 7.5.
# 2. Crie uma variável soma = 0.
# 3. Use o for com .values() para somar todas as notas e achar a média.
# Dica: use len(notas) como divisor para não chumbar números!


notas = {
    "Matematica": 8.0,
    "Historia": 7.5
}


soma = 0

for nota in notas.values():
    soma += nota
    
print(soma)