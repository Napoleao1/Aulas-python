

# Desafio 1: O Banco (Model)
# Crie o arquivo modelo.py. Importe sqlite3. Crie a função criar_tabela() para produtos e a função
# inserir_produto_bd(nome, preco) contendo as lógicas nativas do banco e execução de SQL.

import sqlite3


def conectar():
    return sqlite3.connect("banco.db")


def criar_tabela():
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco real
                )
                """)
        conexao.commit()

    except sqlite3.Error as erro:
        print(f"Ocorreu um erro no banco{erro}")


def inserir_produto_bd(nome, preco):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, preco) VALUES (?, ?)", (nome, preco))
        conexao.commit()


if __name__ == "__main__":
    criar_tabela()