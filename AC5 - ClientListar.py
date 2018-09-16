import requests as Req

url = "http://localhost/alunos"

Retorno = Req.api.get(url).json()

print(Retorno       )
