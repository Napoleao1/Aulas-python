# 1. Conecte-se ao banco loja.db (da aula anterior) e crie o cursor.
# 2. Crie uma função chamada cadastrar_produto().
# 3. Peça ao usuário o nome do produto via input() e o preco (como float).
# 4. Crie o cursor.execute usando INSERT INTO produtos com os curingas seguros ?, ?. Lembre-se de passar a tupla
# com as variáveis!
# 5. Faça o conexao.commit().
# 6. Chame a função 3 vezes para cadastrar 3 produtos.


import sqlite3


def cadastrar_produto():
    while True:
        try:
            nome = input("digite o nome do produto ").strip()
            preco = float(input("digite o preco do produto "))
            
            conexao = sqlite3.connect("loja.db")
            cursor = conexao.cursor()

            cmd_sql = "INSERT INTO  produtos(nome, preco) VALUES (?, ?)"

            cursor.execute(cmd_sql, (nome, preco))

            conexao.commit()
            print("produto cadastrado com sucesso")
            break
        except sqlite3.Error as erro:
            print(f"Erro: {erro}")
            break
        except ValueError:
            print("digite um valor para o produto")
        finally:
            if conexao:
                conexao.close() 
        





# Desafio 2 A Vitrine da Loja Read
# 1. No mesmo arquivo, crie uma função chamada listar_produtos().
# 2. Use o cursor.execute para fazer um SELECT  FROM produtos.
# 3. Pegue os resultados usando uma variável dados = cursor.fetchall().
# 4. Use um laço for linha in dados: para percorrer a variável.
# 5. Imprima cada produto na tela usando f-string. Ex: "Produto: Notebook - R$ 3500.0".

# Dica de ouro: lembre-se de que a linha é uma tupla. Se o banco tem ID, NOME e PREÇO, acesse os valores usando
# os colchetes dos índices: linha[1] e linha[2!.



def listar_produtos():
    try:

        conexao = sqlite3.connect("loja.db")
        cursor = conexao.cursor()


        cursor.execute("SELECT * FROM PRODUTOS")
        
        dados = cursor.fetchall()
        print( "\n--- PRODUTOS ---")
        for produto in dados:
            print(f"{produto[0]} - {produto[1]} - {produto[2]:.2f}")
        
    except sqlite3.Error as erro:
        print(f"Erro: {erro}")
    except ValueError:
        print("digite um valor para o produto")
    finally:
        if conexao:
            conexao.close() 
    
    
listar_produtos()



# 1. Atualize o banco loja.db. Crie a função atualizar_preco().
# 2. Peça ao usuário: "ID do produto" e "Novo preço".
# 3. Use cursor.execute() com UPDATE, passando a tupla segura (novo_preco, id).
# 4. Faça o conexao.commit().
# 5. Use o cursor.rowcount com if/else para avisar se o produto não foi encontrado ou se o preço foi atualizado com
# sucesso. Teste passando um ID real!


def atualizar_preco():
    
    try:

        conexao = sqlite3.connect("loja.db")
        cursor = conexao.cursor()
        id = input("digite o id do produto: ")
        novo_preco = float(input("digite o preco"))
        sql = "UPDATE produtos set preco = ? WHERE id = ?"
        cursor.execute(sql, (novo_preco, id))
        conexao.commit()
        
        if cursor.rowcount == 0:
            print("produto nao encontrado")
        else:
            print(f"Sucesso {cursor.rowcount} linhas(s) alterada(s).")
        
    except sqlite3.Error as erro:
        print(f"Erro: {erro}")
    except ValueError:
        print("digite um valor para o produto")
    
    finally:
        if conexao:
            conexao.close() 

    
    
   
listar_produtos()