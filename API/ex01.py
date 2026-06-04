from flask import Flask, jsonify



app = Flask(__name__)


USUARIOS = [
    {"id": 1, "nome": "sonic", "email": "ernani@gmail.com", "Ativo": True},
    {"id": 2, "nome": "naruto", "email": "teste@gmail.com", "Ativo": True},
    {"id": 3, "nome": "mario", "email": "mario@gmail.com", "Ativo": True}
    ]


@app.route("/api/usuarios/", methods = ["GET"])
def lista_usuarios():