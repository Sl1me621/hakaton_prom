import requests
r=requests.get('http://roboprom.kvantorium33.ru/api/current').json()
print(r)