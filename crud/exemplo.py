init_db()

coenxao = sqlite3.connect('banco_de_dados.db')
cursor = coenxao.cursor()


nome_usuario = input('Digite o nome do usuário: ')
senha_usuario = input("digite sua senha: ")



cmd_sql = "INSERT INTO usuarios (nome, senha) VALUES (?, ?)"

cursor.execute(cmd_sql, (nome_usuario, senha_usuario))

conexao.commit()