from flask import Flask, render_template
app = Flask(__name__)
import requests
from read3cell import readdata, readalldata
def proc_brack():
    data = readalldata()
    y = data[1]['params'][0]['value']
    h = data[5]['params'][0]['value']
    g=(y/h)*100
    return g
def brack_():
    data=readalldata()
    x=data[0]['params'][0]['value']
    y=data[2]['params'][0]['value']
    z=x-y
    return z
def pusk1_():
    data=readalldata()
    f=data[0]['params'][0]['value']
    return f
def pusk2_():
    data=readalldata()
    f=data[1]['params'][0]['value']
    return f
def pusk3_():
    data=readalldata()
    f=data[2]['params'][0]['value']
    return f
def pusk4_():
    data=readalldata()
    f=data[3]['params'][0]['value']
    return f
def pusk5_():
    data=readalldata()
    f=data[4]['params'][0]['value']
    return f
def pusk6_():
    data=readalldata()
    f=data[5]['params'][0]['value']
    return f



def countcellworcks():
    data=readalldata()
    countwoks = 0
    for i in range(6):

        if data[i]['params'][1]['value'] == 1:
            countwoks += 1
    return countwoks
def  weit_countcell():
    data=readalldata()
    countwoks = 0
    for i in range(6):
        if data[i]['params'][1]['value'] == 2:
            countwoks += 1
    return countwoks
def weit_status1():
    data=readalldata()
    c=0
    if data[0]['params'][2]['value'] == 0:
         c = "Нет ожидания"
    if data[0]['params'][2]['value'] == 1:
        c = "Ожидание заготовок"
    if data[0]['params'][2]['value'] == 2:
        c = "Переполнена/ждет след ячейки"
    return c
def weit_status2():
    data=readalldata()
    c=0
    if data[1]['params'][2]['value'] == 0:
         c = "Нет ожидания"
    if data[1]['params'][2]['value'] == 1:
        c = "Ожидание заготовок"
    if data[1]['params'][2]['value'] == 2:
        c = "Переполнена/ждет след ячейки"
    return c
def weit_status3():
    data=readalldata()
    c=0
    if data[2]['params'][2]['value'] == 0:
         c = "Нет ожидания"
    if data[2]['params'][2]['value'] == 1:
        c = "Ожидание заготовок"
    if data[2]['params'][2]['value'] == 2:
        c = "Переполнена/ждет след ячейки"
    return c
def weit_status4():
    data=readalldata()
    c=0
    if data[3]['params'][2]['value'] == 0:
         c = "Нет ожидания"
    if data[3]['params'][2]['value'] == 1:
        c = "Ожидание заготовок"
    if data[3]['params'][2]['value'] == 2:
        c = "Переполнена/ждет след ячейки"
    return c
def weit_status5():
    data=readalldata()
    c=0
    if data[4]['params'][2]['value'] == 0:
         c = "Нет ожидания"
    if data[4]['params'][2]['value'] == 1:
        c = "Ожидание заготовок"
    if data[4]['params'][2]['value'] == 2:
        c = "Переполнена/ждет след ячейки"
    return c
def weit_status6():
    data=readalldata()
    c=0
    if data[5]['params'][2]['value'] == 0:
         c = "Нет ожидания"
    if data[5]['params'][2]['value'] == 1:
        c = "Ожидание заготовок"
    if data[5]['params'][2]['value'] == 2:
        c = "Переполнена/ждет след ячейки"
    return c
def currentwork1():
    data=readalldata()
    c=0
    if data[0]['params'][1]['value'] == 0:
         c = "выключена"
    if data[0]['params'][1]['value'] == 1:
        c = "работает"
    if data[0]['params'][1]['value'] == 2:
        c = "ожидает"
    if data[0]['params'][1]['value'] == 3:
         c = "ошибка"
    return c
def currentwork2():
    data=readalldata()
    c=0
    if data[1]['params'][1]['value'] == 0:
         c = "выключена"
    if data[1]['params'][1]['value'] == 1:
        c = "работает"
    if data[1]['params'][1]['value'] == 2:
        c = "ожидает"
    if data[1]['params'][1]['value'] == 3:
         c = "ошибка"
    return c
def currentwork3():
    data=readalldata()
    c=0
    if data[2]['params'][1]['value'] == 0:
         c = "выключена"
    if data[2]['params'][1]['value'] == 1:
        c = "работает"
    if data[2]['params'][1]['value'] == 2:
        c = "ожидает"
    if data[2]['params'][1]['value'] == 3:
         c = "ошибка"
    return c
def currentwork4():
    data=readalldata()
    c=0
    if data[3]['params'][1]['value'] == 0:
         c = "выключена"
    if data[3]['params'][1]['value'] == 1:
        c = "работает"
    if data[3]['params'][1]['value'] == 2:
        c = "ожидает"
    if data[3]['params'][1]['value'] == 3:
         c = "ошибка"
    return c
def currentwork5():
    data=readalldata()
    c=0
    if data[4]['params'][1]['value'] == 0:
         c = "выключена"
    if data[4]['params'][1]['value'] == 1:
        c = "работает"
    if data[4]['params'][1]['value'] == 2:
        c = "ожидает"
    if data[4]['params'][1]['value'] == 3:
         c = "ошибка"
    return c
def currentwork6():
    data=readalldata()
    c=0
    if data[5]['params'][1]['value'] == 0:
         c = "выключена"
    if data[5]['params'][1]['value'] == 1:
        c = "работает"
    if data[5]['params'][1]['value'] == 2:
        c = "ожидает"
    if data[5]['params'][1]['value'] == 3:
         c = "ошибка"
    return c
def  error_countcell():
    data=readalldata()
    countwoks = 0
    for i in range(6):
        if data[i]['params'][0]['value'] == 3:
            countwoks += 1
    return countwoks
def unworcks_cell():
    data=readalldata()
    countwoks = 0
    for i in range(6):

        if data[i]['params'][1]['value'] == 0:
            countwoks += 1
    return countwoks
@app.route("/")
def home():
    return render_template('index.html')
# Главная страница
@app.route("/main")
def main():
    data = readdata()

    brack=brack_()
    pusk=pusk6_()
    proc_brac=proc_brack()
    coutworcks = countcellworcks()
    countcellunworcks = unworcks_cell()
    countcellweit = weit_countcell()
    countcellerror=error_countcell()
    currentcount1 = currentwork1()
    currentcount2 = currentwork2()
    currentcount3 = currentwork3()
    currentcount4 = currentwork4()
    currentcount5 = currentwork5()
    currentcount6 = currentwork6()
    weitstatus1 = weit_status1()
    weitstatus2 = weit_status2()
    weitstatus3 = weit_status3()
    weitstatus4 = weit_status4()
    weitstatus5 = weit_status5()
    weitstatus6 = weit_status6()
    return render_template('main.html',data=data,coutworcks=coutworcks,countcellunworcks=countcellunworcks,countcellweit=countcellweit,countcellerror=countcellerror,pusk=pusk,currentcount1=currentcount1,currentcount2=currentcount2,currentcount3=currentcount3,currentcount4=currentcount4,currentcount5=currentcount5,currentcount6=currentcount6,
                           weitstatus1 =weitstatus1,proc_brac=proc_brac ,weitstatus2 =weitstatus2,weitstatus3 =weitstatus3 ,weitstatus4 =weitstatus4 ,weitstatus5 =weitstatus5 ,weitstatus6 =weitstatus6,brack=brack)




# Онлайн монитор
@app.route("/online")
def online():
    return render_template('online.html')
# Информация о ячейке
@app.route("/cellinfo")
def cellinfo():
    return render_template('cellinfo.html')
# панель оператора
@app.route("/termoperator")
def termoperator():
    data= readdata()
    currentcount1 = currentwork1()
    currentcount2 = currentwork2()
    currentcount3 = currentwork3()
    currentcount4 = currentwork4()
    currentcount5 = currentwork5()
    currentcount6 = currentwork6()
    return render_template('termoperator.html',currentcount1=currentcount1,currentcount2=currentcount2,currentcount3=currentcount3,currentcount4=currentcount4,currentcount5=currentcount5,currentcount6=currentcount6)

@app.route("/cell1")
def mon_1():
    data = readdata()
    pusk=pusk1_()
    currentcount=currentwork1()
    coutworcks = countcellworcks()
    countcellunworcks = unworcks_cell()
    countcellweit = weit_countcell()
    countcellerror = error_countcell()
    weitstatus = weit_status1()
    return render_template('cell1.html', data=data, coutworcks=coutworcks, countcellunworcks=countcellunworcks,
                           countcellweit=countcellweit, countcellerror=countcellerror,currentcount=currentcount, weitstatus=weitstatus,pusk=pusk)


@app.route("/cell2")
def mon_2():
    data = readdata()
    pusk=pusk2_()
    currentcount = currentwork2()
    coutworcks = countcellworcks()
    countcellunworcks = unworcks_cell()
    countcellweit = weit_countcell()
    countcellerror = error_countcell()
    weitstatus = weit_status2()
    return render_template('cell2.html', data=data, coutworcks=coutworcks, countcellunworcks=countcellunworcks,
                           countcellweit=countcellweit, countcellerror=countcellerror,currentcount=currentcount,weitstatus=weitstatus,pusk=pusk)


@app.route("/cell3")
def mon_3():
    data = readdata()
    pusk=pusk3_()
    currentcount = currentwork3()
    coutworcks = countcellworcks()
    countcellunworcks = unworcks_cell()
    countcellweit = weit_countcell()
    countcellerror = error_countcell()
    weitstatus = weit_status3()
    return render_template('cell3.html', data=data, coutworcks=coutworcks, countcellunworcks=countcellunworcks,
                           countcellweit=countcellweit, countcellerror=countcellerror,currentcount=currentcount,weitstatus=weitstatus,pusk=pusk)


@app.route("/cell4")
def mon_4():
    data = readdata()
    pusk=pusk4_()
    coutworcks = countcellworcks()
    currentcount = currentwork4()
    countcellunworcks = unworcks_cell()
    countcellweit = weit_countcell()
    countcellerror = error_countcell()
    weitstatus = weit_status4()
    return render_template('cell4.html', data=data, coutworcks=coutworcks, countcellunworcks=countcellunworcks,
                           countcellweit=countcellweit, countcellerror=countcellerror,currentcount=currentcount,weitstatus=weitstatus,pusk=pusk)


@app.route("/cell5")
def mon_5():
    data = readdata()
    coutworcks = countcellworcks()
    pusk=pusk5_()
    currentcount = currentwork5()
    countcellunworcks = unworcks_cell()
    countcellweit = weit_countcell()
    countcellerror = error_countcell()
    weitstatus = weit_status5()
    return render_template('cell5.html', data=data, coutworcks=coutworcks, countcellunworcks=countcellunworcks,
                           countcellweit=countcellweit, countcellerror=countcellerror,currentcount=currentcount,weitstatus=weitstatus,pusk=pusk)


@app.route("/cell6")
def mon_6():
    data = readdata()
    pusk=pusk6_()
    coutworcks = countcellworcks()
    currentcount = currentwork6()
    countcellunworcks = unworcks_cell()
    countcellweit = weit_countcell()
    countcellerror = error_countcell()
    weitstatus = weit_status6()
    return render_template('cell6.html', data=data, coutworcks=coutworcks, countcellunworcks=countcellunworcks,
                           countcellweit=countcellweit, countcellerror=countcellerror,currentcount=currentcount,weitstatus=weitstatus,pusk=pusk)


@app.route("/mon_cell1")
def mon_7():
    data = readdata()
    currentcount = currentwork1()
    weitstatus = weit_status1()
    return render_template('mon_cell1.html', data=data, currentcount=currentcount, weitstatus=weitstatus)
@app.route("/mon_cell2")
def mon_8():
    data = readdata()
    currentcount = currentwork2()
    weitstatus = weit_status2()
    return render_template('mon_cell2.html', data=data, currentcount=currentcount, weitstatus=weitstatus)
@app.route("/mon_cell3")
def mon_9():
    data = readdata()
    currentcount = currentwork3()
    weitstatus = weit_status3()
    return render_template('mon_cell3.html', data=data, currentcount=currentcount, weitstatus=weitstatus)
@app.route("/mon_cell4")
def mon_10():
    data = readdata()
    currentcount = currentwork4()
    weitstatus = weit_status4()
    return render_template('mon_cell4.html', data=data, currentcount=currentcount, weitstatus=weitstatus)
@app.route("/mon_cell5")
def mon_11():
    data = readdata()
    currentcount = currentwork5()
    weitstatus = weit_status5()
    return render_template('mon_cell5.html', data=data, currentcount=currentcount, weitstatus=weitstatus)
@app.route("/mon_cell6")
def mon_12():
   data = readdata()
   currentcount = currentwork6()
   weitstatus =weit_status6()
   return render_template('mon_cell6.html',data=data, currentcount=currentcount,weitstatus=weitstatus)

if __name__=="__main__":
    app.run(debug=True)