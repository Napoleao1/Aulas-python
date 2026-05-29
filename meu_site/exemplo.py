from flask import Flask, request


app = Flask(__name__)


@app.route('/dobro/<int:numero>')
def calculadora(numero):
    return (f"o dobro de {numero} é {numero * 2}")


@app.route('/loja')
def listar_produtos():
    categoria = request.args.get('categoria')
    if categoria:
        return f"mostrando produtos: {categoria}"
    else:
        return "mostrando todos os produtos"

if __name__ == '__main__':
    app.run(debug=True)
