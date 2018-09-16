import requests as Req

url = "http://localhost/alunos"
aluno = {"Ra":1700637, "Nome":"Ícaro Guedes", "Status":"Ativo"}

Retorno = Req.api.post(url, json=aluno).json()

print(Retorno)
