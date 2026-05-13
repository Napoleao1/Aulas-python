# Desafio 1 O Sistema da Loja
# 1. Crie uma conexão com um banco loja.db (use o try/except/finally).
# 2. Crie o cursor e faça o cursor.execute para criar uma tabela produtos.
# 3. Colunas: id Inteiro, Chave Primária), nome Texto e preco REAL.
# 4. Faça o commit() e rode o código. Veja a tabela no SQLite Viewer!
# Desafio 2 O Controle de Estoque
# 1. No mesmo arquivo, adicione um SEGUNDO cursor.execute() logo abaixo.
# 2. Crie uma nova tabela chamada fornecedores contendo id Chave Primária), empresa Texto e telefone Texto.
# 3. Execute o código de novo e confira se o banco agora possui duas tabelas!


import sqlite3

try:
    conexao = sqlite3.connect("loja.db")
    cursor = conexao.cursor()
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY,
        nome TEXT, preco REAL
        )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fornecedores(
        ID INTEGER PRIMARY KEY,
        empresa TEXT, telefone TEXT,
        )
    """)

    conexao.commit()
    print("banco configurado")
except sqlite3.Error as erro:
    print(f"Erro: {erro}")
finally:
    if conexao:
        conexao.close() 
        


