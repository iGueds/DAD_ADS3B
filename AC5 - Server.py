from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

lista_alunos = []

response = {"Status": "", "Dados": "", "Mensagem": ""}


@app.route('/alunos', methods=['GET'])
def alunos():
        response['Status'] = "OK"
        response['Mensagem'] = "Consulta realizada."
        response['Dados'] = lista_alunos
        return jsonify(response)


@app.route('/alunos', methods=['POST'])
def cadastrarAluno():
        Dados = request.get_json()
        lista_alunos.append({"Ra": int(Dados["Ra"]), "Nome": Dados['Nome'], "Status": Dados["Status"]})
        response['Status'] = "OK"
        response['Mensagem'] = "Aluno cadastrado!"
        response['Dados'] = lista_alunos
        return jsonify(response)


@app.route('/alunos/consulta/<int:Ra>', methods=['GET'])
def consultaAluno(Ra):
    for i in lista_alunos:
        if i["Ra"] == Ra:
            response['Status'] = "OK"
            response['Mensagem'] = "Consulta realizada."
            response['Dados'] = i
        else:
            response['Status'] = "Erro"
            response['Mensagem'] = "Aluno não encontrado."

    return jsonify(response)


@app.route('/alunos/atualizar/<int:Ra>', methods=['PUT'])
def atualizarAluno(Ra):

    Dados = request.get_json()

    for i in lista_alunos:
        if i["Ra"] == Ra:
            i["Ra"] = Dados["Ra"]
            i["Nome"] = Dados["Nome"]
            response['Dados'] = lista_alunos
            response['Status'] = "OK"
            response['Mensagem'] = "Aluno atualizado."
            break

        else:
            response['Status'] = "Erro"
            response['Mensagem'] = "Aluno não encontrado."

    return jsonify(response)


@app.route('/alunos/deletar/<int:Ra>', methods=['DELETE'])
def deletarAluno(Ra):
    for i in lista_alunos:
        if i["Ra"] == Ra:
            lista_alunos.remove(i)
            response['Dados'] = i
            response['Status'] = "OK"
            response['Mensagem'] = "Aluno deletado."
        else:
            response['Status'] = "Erro"
            response['Mensagem'] = "Aluno não encontrado."
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=80)


#Da um 10 aí professor, que essa aqui eu tava inspirado pra fazer