import requests as Req

#Request Temperatura São Paulo

Url = 'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/3477/current?token=48c2325fa5148ee73a6e9c1b4d1890b7'

t_sp = Req.api.get(Url).json()

tempo_sp = (t_sp['data']['temperature'])

print("A temperatura em São Paulo é:", tempo_sp)

#Request Temperatura Recife

Url = 'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/7140/current?token=48c2325fa5148ee73a6e9c1b4d1890b7'

t_rcf = Req.api.get(Url).json()

tempo_rcf = (t_rcf['data']['temperature'])

print("A temperatura em Recife é:", tempo_rcf)


#Request Temperatura Fortaleza

Url = 'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/8050/current?token=48c2325fa5148ee73a6e9c1b4d1890b7'

t_ftz = Req.api.get(Url).json()

tempo_ftz = (t_ftz['data']['temperature'])

print("A temperatura em Fortaleza é:", tempo_ftz)
