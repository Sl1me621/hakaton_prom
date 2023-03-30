import requests
def readdata():
    r=requests.get('http://roboprom.kvantorium33.ru/api/current?cell=3').json()
    if r['result']=='success':
        return r['data']
# readdata()

def readalldata():
    r = requests.get('http://roboprom.kvantorium33.ru/api/current').json()
    print(r)
    if r['result'] == 'success':
        # for i in range(6):
        #     print(r['data'][i]['params'][0]['value'])

        return r['data']
readalldata()