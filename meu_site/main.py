import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/')
def pagina_incial():
    return "Bem-vindo ao meus site"


@app.route('/contato')
def pagina_contato():
    return "Entre em contato comigo pelo email:"


@app.route('/hora')
def pagina_hora():
    agora = datetime.datetime.now()
    return agora.strftime("Agora são %H:%M:%S do dia %d/%m/%Y")


if __name__ == '__main__':
    app.run(debug=True)
