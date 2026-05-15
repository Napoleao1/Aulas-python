import customtkinter as ctk
from banco import conectar


def cadastrar():
    nome_digitado = caixa_nome.get()
    quantidade_texto = caixa_quantidade.get()

    if nome_digitado == "" or quantidade_texto == "":
        lbl_mensagem.configure(
            text="Preencha todos os campos!",
            text_color="red"
        )
        return

    quantidade_digitado = int(quantidade_texto)

    conexao = conectar()
    cursor = conexao.cursor()

    cmd_sql = """
    INSERT INTO produtos (nome_produto, quantidade)
    VALUES (?, ?)
    """

    cursor.execute(cmd_sql, (nome_digitado, quantidade_digitado))

    conexao.commit()
    conexao.close()

    lbl_mensagem.configure(
        text="Cadastrado!",
        text_color="green"
    )

    caixa_nome.delete(0, "end")
    caixa_quantidade.delete(0, "end")

    atualizar_lista_visual()


def buscar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")
    dados = cursor.fetchall()

    conexao.close()

    return dados


def atualizar_lista_visual():
    area_lista.delete("0.0", "end")

    produtos = buscar_produtos()

    for produto in produtos:
        texto = f"ID: {produto[0]} | {produto[1]} | Quantidade: {produto[2]}\n"
        area_lista.insert("end", texto)


def excluir_produto():
    id_dig = cx_id_excluir.get()

    if id_dig == "":
        return

    con = conectar()
    cur = con.cursor()

    cur.execute(
        "DELETE FROM produtos WHERE id = ?",
        (id_dig,)
    )

    con.commit()

    if cur.rowcount == 0:
        lbl_mensagem.configure(
            text="ID não encontrado!",
            text_color="red"
        )
    else:
        lbl_mensagem.configure(
            text="Produto excluído!",
            text_color="green"
        )

        cx_id_excluir.delete(0, "end")

    con.close()

    atualizar_lista_visual()


# ================= JANELA =================

janela = ctk.CTk()
janela.geometry("500x500")
janela.title("Cadastro de Produtos")

lbl_titulo = ctk.CTkLabel(
    janela,
    text="NOVO PRODUTO"
)
lbl_titulo.pack(pady=20)

caixa_nome = ctk.CTkEntry(
    janela,
    placeholder_text="Nome do Produto"
)
caixa_nome.pack(pady=10)

caixa_quantidade = ctk.CTkEntry(
    janela,
    placeholder_text="Quantidade"
)
caixa_quantidade.pack(pady=10)

btn_cadastrar = ctk.CTkButton(
    janela,
    text="Salvar",
    command=cadastrar
)
btn_cadastrar.pack(pady=20)

lbl_mensagem = ctk.CTkLabel(
    janela,
    text=""
)
lbl_mensagem.pack()

area_lista = ctk.CTkTextbox(
    janela,
    width=350,
    height=150
)
area_lista.pack(pady=10)

cx_id_excluir = ctk.CTkEntry(
    janela,
    placeholder_text="ID para excluir"
)
cx_id_excluir.pack(pady=5)

btn_excluir = ctk.CTkButton(
    janela,
    text="Excluir",
    fg_color="red",
    hover_color="darkred",
    command=excluir_produto
)
btn_excluir.pack(pady=10)

atualizar_lista_visual()

janela.mainloop()