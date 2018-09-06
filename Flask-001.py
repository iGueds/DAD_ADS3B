from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/ola', methods=["GET"])
def RespostaOla():
    Dados = {"Mensagem":"Olá dono do morro"}
    Resposta = jsonify(Dados)
    return Resposta

if __name__ == "__main__":
    app.run()
