import requests as Req

Url = 'http://www.omdbapi.com/?apikey=fb7ee6ee&i=tt3748528'

Retorno = Req.api.get(Url).json()

print(Retorno)