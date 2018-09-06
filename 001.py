import requests as Req

Url = 'http://img.omdbapi.com/?apikey=fb7ee6ee&i=tt0075984'

Retorno = Req.api.get(Url).content

print(Retorno)

with open("Teste01.jpg", "wb") as QQ:
    QQ.write(Retorno)