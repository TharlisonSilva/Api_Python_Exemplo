from flask import Flask, json, jsonify,request

from Controllers import alunoController


app   = Flask(__name__)
aluno = alunoController.Aluno()

@app.route("/")
def ok():
    return "Tudo Ok!"

@app.route("/Cadastra/Aluno", methods=["POST"])
def ChamaController():
    body = request.get_json()
    return aluno.Create(body["Nome"], body["Sobrenome"])

app.run(port=5000, debug=False)