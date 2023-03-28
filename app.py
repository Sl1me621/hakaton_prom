from flask import Flask, render_template

import requests

app = Flask(__name__)
import json
name='Имя'
def readData():...

def readApi():
    r = requests.get('http://roboprom.kvantorium33.ru/api/current').json()
    return (r['data'])
@app.route("/")
def home():

    return render_template('main.html')
@app.route("/table")
def table():
    return render_template('table.html')
@app.route("/cell1")
def mon():
    cellinfo = readApi()
    return  render_template('cell1.html', cellinfo=cellinfo)
##@app.route("/cell2")
#def mon():
 #   cellinfo = readApi()
 #   return  render_template('cell2.html', cellinfo=cellinfo)
#@app.route("/cell3")
#def mon():
 #   cellinfo = readApi()
 #  return  render_template('cell3.html', cellinfo=cellinfo)
#@app.route("/cell4")
#def mon():
 #   cellinfo = readApi()
 #   return  render_template('cell4.html', cellinfo=cellinfo)
#@app.route("/cell5")
#def mon():
 #   cellinfo = readApi()
 #   return  render_template('cell5.html', cellinfo=cellinfo)
#@app.route("/cell6")
#@def mon():
  #  cellinfo = readApi()
  #  return  render_template('cell6.html', cellinfo=cellinfo)

#@app.route("")
#def team():
  #  allteam= readApi()
 #   return render_template('team.html',allteam=allteam)
#@app.route("/allinfo")
def allinfo():
    return render_template('allinfo.html')
if __name__=="__main__":
    app.run(debug=True)