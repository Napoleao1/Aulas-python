# Crie o arquivo tela.py. Importe o CustomTkinter e from controlador import validar_produto.

# Desenhe a janela com entradas e botão. A função do botão deve extrair os textos com .get() e repassar
# chamando a função do Cérebro. Teste e veja o dado viajar por 3 arquivos até chegar ao banco de dados!


import customtkinter as CTk

from controllers.controller import validar_produto

janela = CTk.CTk()
entrada_nome = CTk.CTkEntry(janela, placeholder_text="Nome do produto")
entrada_nome.pack(pady=10)
entrada_preco = CTk.CTkEntry(janela, placeholder_text="Preço")
entrada_preco.pack(pady=10)

def cadastrar():
    nome = entrada_nome.get()
    preco = entrada_preco.get()
    validar_produto(nome, preco)


botao = CTk.CTkButton(janela, text="Cadastrar", command=cadastrar)
botao.pack(pady=10)

janela.mainloop()
