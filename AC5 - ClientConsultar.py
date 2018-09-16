import requests as Req

url = "http://localhost/alunos/consulta/1700637"

Retorno = Req.api.get(url).json()

print(Retorno)
