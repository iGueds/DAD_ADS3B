import requests as Req

Url = "http://localhost/alunos/atualizar/1700637"
Produto = {"Nome":"Pedro Henrique", "Ra":1700627}

Retorno = Req.api.put(Url, json=Produto).json()
print(Retorno)