from flask import Flask
from flask import jsonify
from flask import request
import uuid
App = Flask(__name__)

Resposta = {"Status":"","Dados":"","Mensagem":""}
Produtos = []

@App.route('/produtos', methods=["GET"])
def listarProdutos():
    Resposta["Status"] = "Sucesso"
    Resposta["Mensagem"] = ""
    Resposta["Dados"] = Produtos
    return jsonify(Resposta)

@App.route('/produtos/cadastrar', methods=["POST"])
def CadastrarProduto():
    Dados = request.get_json()
    Id = uuid.uuid1()
    Nome = Dados["Nome"]
    Preco = Dados["Preco"]
    Produtos.append({"Id":Id, "Nome":Nome, "Preco":Preco})

    Resposta["Status"] = "Sucesso"
    Resposta["Mensagem"] = "Produto cadastrado"
    Resposta["Dados"] = Produtos
    return jsonify(Resposta)

if __name__ == "__main__":
    App.run(port=80)