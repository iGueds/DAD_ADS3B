from flask import Flask
from flask import jsonify

app = Flask(__name__)
def listaAlunos():
    alunos = {
        1:'Ícaro Guedes',
        2:'José Ricardo',
        3:'Kevin Prado',
        4:'Gustavo Serafim',
        5:'Guilherme Alcântara'
    }
    return jsonify(alunos)

@app.route('/aluno', methods=["GET"])
def listar():
    return listaAlunos()

if __name__ == "__main__":
    app.run(port=80)
