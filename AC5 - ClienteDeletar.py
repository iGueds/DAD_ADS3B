import requests as Req

url = "http://localhost/alunos/deletar/1700627"

Retorno = Req.api.delete(url).json()

print(Retorno)
