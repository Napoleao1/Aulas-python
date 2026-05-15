import sqlite3 # importando o sql
import customtkinter as ctk

# 1. Crie uma função para conectar ao banco estoque_app.db e criar uma tabela produtos (colunas: id, nome_produto e
# quantidade INTEGER).


def conectar():
    return sqlite3.connect("clientes_app.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_produto TEXT NOT NULL,
            quantidade INTEGER
        )
    """)
    
    conexao.commit()
    conexao.close()
    
    
    
criar_tabela()