from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", method = "GET")
def index():
    return jsonify({"status": "sucesso"})


@app.route("/api/produtos/<int:id_produto", methods=["GET"])
def obter_produto(id_produto):
    produto_encontrado = None
    for produto in PRODUTOS:
        if produto["id"] == id_produto:
            produto_encontrado = produto
            break
    if produto_encontrado is None:
        return jsonify({
            "erro": "PRODUTO_NAO_ECONTRADO",
            "mensagem": f"ID {id_produto} inexistente"
        }), 404
        
        return jsonify(produto_encontrado), 200

if __name__ == "__main__":
    app.run(debug=True)