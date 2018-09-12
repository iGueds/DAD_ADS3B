import requests as Req

url = "http://localhost/produtos/cadastrar"
Produto = {"Nome":"TV 50 Pol.", "Preco":1999}

Retorno = Req.api.post(url, json=Produto).json()

print(Retorno)
