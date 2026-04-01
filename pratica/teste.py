# Cadastros no "banco de dados"
user_bd = "admin"
senha_bd = "1234"

# Tentativa do usuário (input)
user = input("User: ")
pwd = input("Senha: ")

# Operador 'and' junta a validação!
acesso = (user == user_bd) and (pwd ==senha_bd)

print(f"Acesso Liberado? {acesso}")