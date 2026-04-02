# Desafio 1 O Perfil do Usuário
# 1. Crie um dicionário perfil contendo 3 chaves: "nome", "idade" e "email". Preencha com seus dados reais.
# 2. Imprima uma frase formatada acessando as chaves. Exemplo: "Olá [nome], vi que você tem [idade]
# anos e seu e-mail é [email]."


info = {
    "nome": "ernani",
    "idade": "25",
    "email": "ernaninandoxd@gmail.com"   
}

print(f"Ola {info["nome"]}, vi que voce tem {info["idade"]} anos e seu email é {info["email"]}" )