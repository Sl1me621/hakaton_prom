import requests
def readdata():
    r=requests.get('http://roboprom.kvantorium33.ru/api/current?cell=3').json()
    if r['result']=='success':
        print(r['data'])
        return r['data']
# readdata()

def readalldata():
    r = requests.get('http://roboprom.kvantorium33.ru/api/current').json()
    print(r)
    if r['result'] == 'success':
        print(r['data'])
        # for i in range(6):
        #     print(r['data'][i]['params'][0]['value'])

        return r['data']

<<<<<<< HEAD
=======


>>>>>>> be955e458cd5bc3b5d13a2627756e09a1fabf048
readalldata()