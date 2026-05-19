import sqlite3

def conectar():
    return sqlite3.connect("banco.db")


def criar_tabela()
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            
            
            cursor.execute("""
                CREATE TABLE)