import requests as Req

Url = 'http://localhost/aluno'

lista = Req.api.get(Url).json()

for i in lista:
    alunos = (lista[i])
    print("O aluno", alunos, "tem ID =", i)