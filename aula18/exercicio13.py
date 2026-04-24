# 13. Salvando uma Configuração (Aulas 12 e 20)
# O que deve fazer: 1. Crie um dicionário: config = {"resolucao": "1920x1080", "volume": 80}.
# 2. Importe o json e use um bloco with open("config.json", "w") juntamente com json.dump() para
# gravar o ficheiro no seu disco.
# 3. Agora "simule" a reinicialização do jogo: em código, apague a sua variável (ou crie um bloco
# de leitura novo com with open("config.json", "r")), carregue os dados com json.load(), mude a
# chave "volume" para 50 e imprima o dicionário final para comprovar que leu com sucesso.

import json

config = {"resolucao": "1920x1080", "volume": 80}

with open("config.json", "w") as arquivo:
    json.dump(config, arquivo)
    
with open("config.json", "r") as arquivo:
    config_lido = json.load(arquivo)
    
    config_lido["volume"] = 50
    
print(config_lido)