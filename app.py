from flask import Flask, render_template
app = Flask(__name__)
import requests
from read3cell import readdata, readalldata
def speed_ln():
    data=readalldata()
    f = data[5]['params'][0]['value']
    g=f/24
    return g
def weitstatus1():
    wstatusd1=0
    if weit_status1_1()==1:
        wstatusd1=wstatus_d1()
    if weit_status1_1()==0:
        wstatusd1=wstatus_d1_0()
    if weit_status1_1()==2:
        wstatusd1=wstatus_d1_2()
    return wstatusd1
def weitstatus2():
    wstatusd2=0
    if weit_status2_2()==1:
        wstatusd2=wstatus_d2()
    if weit_status2_2()==0:
        wstatusd2=wstatus_d2_0()
    if weit_status2_2()==2:
        wstatusd2=wstatus_d2_2()
    return wstatusd2
def weitstatus3():
    wstatusd3=0
    if weit_status3_3()==1:
        wstatusd3=wstatus_d3()
    if weit_status3_3()==0:
        wstatusd3=wstatus_d3_0()
    if weit_status3_3()==2:
        wstatusd3=wstatus_d3_2()
    return wstatusd3
def weitstatus4():
    wstatusd4=0
    if weit_status4_4()==1:
        wstatusd4=wstatus_d4()
    if weit_status4_4()==0:
        wstatusd4=wstatus_d4_0()
    if weit_status4_4()==2:
        wstatusd4=wstatus_d4_2()
    return wstatusd4
def weitstatus5():
    wstatusd5=0
    if weit_status5_5()==1:
        wstatusd5=wstatus_d5()
    if weit_status5_5()==0:
        wstatusd5=wstatus_d5_0()
    if weit_status5_5()==2:
        wstatusd5=wstatus_d5_2()
    return wstatusd5
def weitstatus6():
    wstatusd6=0
    if weit_status6_6()==1:
        wstatusd6=wstatus_d6()
    if weit_status6_6()==0:
        wstatusd6=wstatus_d6_0()
    if weit_status6_6()==2:
        wstatusd6=wstatus_d6_2()
    return wstatusd6
def wstatush1():
    wstatush1=0
    if weit_status1_1()==1:
        wstatush1=wstatus_h1()
    if weit_status1_1()==0:
        wstatush1=wstatus_h1_0()
    if weit_status1_1()==2:
       wstatush1=wstatus_h1_2()
    return wstatush1
def wstatush2():
    wstatush2=0
    if weit_status2_2()==1:
        wstatush2=wstatus_h2()
    if weit_status2_2()==0:
        wstatush2=wstatus_h2_0()
    if weit_status2_2()==2:
       wstatush2=wstatus_h2_2()
    return wstatush2

def wstatush3():
    wstatush3=0
    if weit_status3_3()==1:
        wstatush3=wstatus_h3()
    if weit_status3_3()==0:
        wstatush3=wstatus_h3_0()
    if weit_status3_3()==2:
       wstatush3=wstatus_h3_2()
    return wstatush3
def wstatush4():
    wstatush4=0
    if weit_status4_4()==1:
        wstatush4=wstatus_h4()
    if weit_status4_4()==0:
        wstatush4=wstatus_h4_0()
    if weit_status4_4()==2:
       wstatush4=wstatus_h4_2()
    return wstatush4
def wstatush5():
    wstatush5=0
    if weit_status5_5()==1:
        wstatush5=wstatus_h5()
    if weit_status5_5()==0:
        wstatush5=wstatus_h5_0()
    if weit_status5_5()==2:
       wstatush5=wstatus_h5_2()
    return wstatush5
def wstatush6():
    wstatush6=0
    if weit_status6_6()==1:
        wstatush6=wstatus_h6()
    if weit_status6_6()==0:
        wstatush6=wstatus_h6_0()
    if weit_status6_6()==2:
       wstatush6=wstatus_h6_2()
    return wstatush6
def wstatus_h1():
    data=readalldata()
    wtatush=data[0]['wait_h'][1]
    return  wtatush
def wstatus_h2():
    data=readalldata()
    wtatush=data[1]['wait_h'][1]
    return  wtatush
def wstatus_h3():
    data=readalldata()
    wtatush=data[2]['wait_h'][1]
    return  wtatush
def wstatus_h4():
    data=readalldata()
    wtatush=data[3]['wait_h'][1]
    return  wtatush
def wstatus_h5():
    data=readalldata()
    wtatush=data[4]['wait_h'][1]
    return  wtatush
def wstatus_h6():
    data=readalldata()
    wtatush=data[5]['wait_h'][1]
    return  wtatush
def wstatus_h1_0():
    data=readalldata()
    wstatush=data[0]['wait_h'][0]
    return  wstatush
def wstatus_h2_0():
    data=readalldata()
    wstatush=data[1]['wait_h'][0]
    return  wstatush
def wstatus_h3_0():
    data=readalldata()
    wstatush=data[2]['wait_h'][0]
    return  wstatush
def wstatus_h4_0():
    data=readalldata()
    wstatush=data[3]['wait_h'][0]
    return  wstatush
def wstatus_h5_0():
    data=readalldata()
    wstatush=data[4]['wait_h'][0]
    return  wstatush
def wstatus_h6_0():
    data=readalldata()
    wstatush=data[5]['wait_h'][0]
    return  wstatush
def wstatus_h1_2():
    data=readalldata()
    wtatush=data[0]['wait_h'][2]
    return  wtatush
def wstatus_h2_2():
    data=readalldata()
    wtatush=data[1]['wait_h'][2]
    return  wtatush
def wstatus_h3_2():
    data=readalldata()
    wtatush=data[2]['wait_h'][2]
    return  wtatush
def wstatus_h4_2():
    data=readalldata()
    wtatush=data[3]['wait_h'][2]
    return  wtatush
def wstatus_h5_2():
    data=readalldata()
    wtatush=data[4]['wait_h'][2]
    return  wtatush
def wstatus_h6_2():
    data=readalldata()
    wtatush=data[5]['wait_h'][2]
    return  wtatush
def wstatus_d1():
    data=readalldata()
    wstatusd=data[0]['wait_d'][1]
    return  wstatusd
def wstatus_d2():
    data=readalldata()
    wstatusd=data[1]['wait_d'][1]
    return  wstatusd
def wstatus_d3():
    data=readalldata()
    wstatusd=data[2]['wait_d'][1]
    return  wstatusd
def wstatus_d4():
    data=readalldata()
    wstatusd=data[3]['wait_d'][1]
    return  wstatusd
def wstatus_d5():
    data=readalldata()
    wstatusd=data[4]['wait_d'][1]
    return  wstatusd
def wstatus_d6():
    data=readalldata()
    wstatusd=data[5]['wait_d'][1]
    return  wstatusd
def wstatus_d1_0():
    data=readalldata()
    wstatusd=data[0]['wait_d'][0]
    return  wstatusd
def wstatus_d2_0():
    data=readalldata()
    wstatusd=data[1]['wait_d'][0]
    return  wstatusd
def wstatus_d3_0():
    data=readalldata()
    wstatusd=data[2]['wait_d'][0]
    return  wstatusd
def wstatus_d4_0():
    data=readalldata()
    wstatusd=data[3]['wait_d'][0]
    return  wstatusd
def wstatus_d5_0():
    data=readalldata()
    wstatusd=data[4]['wait_d'][0]
    return  wstatusd
def wstatus_d6_0():
    data=readalldata()
    wstatusd=data[5]['wait_d'][0]
    return  wstatusd
def wstatus_d1_2():
    data=readalldata()
    wstatusd=data[0]['wait_d'][2]
    return  wstatusd
def wstatus_d2_2():
    data=readalldata()
    wstatusd=data[1]['wait_d'][2]
    return  wstatusd
def wstatus_d3_2():
    data=readalldata()
    wstatusd=data[2]['wait_d'][2]
    return  wstatusd
def wstatus_d4_2():
    data=readalldata()
    wstatusd=data[3]['wait_d'][2]
    return  wstatusd
def wstatus_d5_2():
    data=readalldata()
    wstatusd=data[4]['wait_d'][2]
    return  wstatusd
def wstatus_d6_2():
    data=readalldata()
    wstatusd=data[5]['wait_d'][2]
    return  wstatusd
def wstatush_proch1():
    wstatusproc1=wstatush1()
    wstatusproc1=wstatusproc1/3600
    wstatusproc1=wstatusproc1*100
    return wstatusproc1
def wstatush_proch2():
    wstatusproc2=wstatush2()
    wstatusproc2=wstatusproc2/3600
    wstatusproc2=wstatusproc2*100
    return wstatusproc2

def wstatush_proch3():
    wstatusproc3=wstatush3()
    wstatusproc3=wstatusproc3/3600
    wstatusproc3=wstatusproc3*100
    return wstatusproc3
def wstatush_proch4():
    wstatusproc4=wstatush4()
    wstatusproc4=wstatusproc4/3600
    wstatusproc4=wstatusproc4*100
    return wstatusproc4
def wstatush_proch5():
    wstatusproc5=wstatush5()
    wstatusproc5=wstatusproc5/3600
    wstatusproc5=wstatusproc5*100
    return wstatusproc5
def wstatush_proch6():
    wstatusproc6=wstatush6()
    wstatusproc6=wstatusproc6/3600
    wstatusproc6=wstatusproc6*100
    return wstatusproc6
def wstatusd_proc1():
    wstatusproc1=weitstatus1()
    wstatusproc1=wstatusproc1/86400
    wstatusproc1=wstatusproc1*100
    return wstatusproc1
def wstatusd_proc2():
    wstatusproc2=weitstatus2()
    wstatusproc2=wstatusproc2/86400
    wstatusproc2=wstatusproc2*100
    return wstatusproc2
def wstatusd_proc3():
    wstatusproc3=weitstatus3()
    wstatusproc3=wstatusproc3/86400
    wstatusproc3=wstatusproc3*100
    return wstatusproc3
def wstatusd_proc4():
    wstatusproc4=weitstatus4()
    wstatusproc4=wstatusproc4/86400
    wstatusproc4=wstatusproc4*100
    return wstatusproc4
def wstatusd_proc5():
    wstatusproc5=weitstatus5()
    wstatusproc5=wstatusproc5/86400
    wstatusproc5=wstatusproc5*100
    return wstatusproc5
def wstatusd_proc6():
    wstatusproc6=weitstatus6()
    wstatusproc6=wstatusproc6/86400
    wstatusproc6=wstatusproc6*100
    return wstatusproc6
def statush1():
    statush=0
    if currentwork1_1()==1:
        statush=status_h1()
    if currentwork1_1()==0:
        statush=status_h1_0()
    if currentwork1_1()==2:
        statush=status_h1_2()
    if currentwork1_1()==3:
        statush=status_h1_3()
    return statush
def statush2():
    statush=0
    if currentwork2_2()==1:
        statush=status_h2()
    if currentwork2_2()==0:
        statush=status_h2_0()
    if currentwork2_2()==2:
        statush=status_h2_2()
    if currentwork2_2()==3:
        statush=status_h2_3()
    return statush
def statush3():
    statush=0
    if currentwork3_3()==1:
        statush=status_h3()
    if currentwork3_3()==0:
        statush=status_h3_0()
    if currentwork3_3()==2:
        statush=status_h3_2()
    if currentwork3_3()==3:
        statush=status_h3_3()
    return statush
def statush4():
    statush=0
    if currentwork4_4()==1:
        statush=status_h4()
    if currentwork4_4()==0:
        statush=status_h4_0()
    if currentwork4_4()==2:
        statush=status_h4_2()
    if currentwork4_4()==3:
        statush=status_h4_3()
    return statush
def statush5():
    statush=0
    if currentwork5_5()==1:
        statush=status_h5()
    if currentwork5_5()==0:
        statush=status_h5_0()
    if currentwork5_5()==2:
        statush=status_h5_2()
    if currentwork5_5()==3:
        statush=status_h5_3()
    return statush
def statush6():
    statush=0
    if currentwork6_6()==1:
        statush=status_h6()
    if currentwork6_6()==0:
        statush=status_h6_0()
    if currentwork6_6()==2:
        statush=status_h6_2()
    if currentwork6_6()==3:
        statush=status_h6_3()
    return statush
def status_h1():
    data=readalldata()
    statush=data[0]['status_h'][1]
    return  statush
def status_h2():
    data=readalldata()
    statush=data[1]['status_h'][1]
    return  statush

def status_h3():
    data=readalldata()
    statush=data[2]['status_h'][1]
    return  statush

def status_h4():
    data=readalldata()
    statush=data[3]['status_h'][1]
    return  statush

def status_h5():
    data=readalldata()
    statush=data[4]['status_h'][1]
    return  statush

def status_h6():
    data=readalldata()
    statush=data[5]['status_h'][1]
    return  statush

def status_h1_0():
    data=readalldata()
    statush=data[0]['status_h'][0]
    return  statush
def status_h2_0():
    data=readalldata()
    statush=data[1]['status_h'][0]
    return  statush
def status_h3_0():
    data=readalldata()
    statush=data[2]['status_h'][0]
    return  statush
def status_h4_0():
    data=readalldata()
    statush=data[3]['status_h'][0]
    return  statush
def status_h5_0():
    data=readalldata()
    statush=data[4]['status_h'][0]
    return  statush
def status_h6_0():
    data=readalldata()
    statush=data[5]['status_h'][0]
    return  statush
def status_h1_2():
    data=readalldata()
    statush=data[0]['status_h'][2]
    return  statush
def status_h2_2():
    data=readalldata()
    statush=data[1]['status_h'][2]
    return  statush
def status_h3_2():
    data=readalldata()
    statush=data[2]['status_h'][2]
    return  statush
def status_h4_2():
    data=readalldata()
    statush=data[3]['status_h'][2]
    return  statush
def status_h5_2():
    data=readalldata()
    statush=data[4]['status_h'][2]
    return  statush
def status_h6_2():
    data=readalldata()
    statush=data[5]['status_h'][2]
    return  statush
def status_h1_3():
    data=readalldata()
    statush=data[0]['status_h'][3]
    return  statush
def status_h2_3():
    data=readalldata()
    statush=data[1]['status_h'][3]
    return  statush
def status_h3_3():
    data=readalldata()
    statush=data[2]['status_h'][3]
    return  statush
def status_h4_3():
    data=readalldata()
    statush=data[3]['status_h'][3]
    return  statush
def status_h5_3():
    data=readalldata()
    statush=data[4]['status_h'][3]
    return  statush
def status_h6_3():
    data=readalldata()
    statush=data[5]['status_h'][3]
    return  statush
def statush_proch1():
    statusproc1=statush1()
    statusproc1=statusproc1/3600
    statusproc1=statusproc1*100
    return statusproc1
def statush_proch2():
    statusproc2=statush2()
    statusproc2=statusproc2/3600
    statusproc2=statusproc2*100
    return statusproc2

def statush_proch3():
    statusproc3=statush3()
    statusproc3=statusproc3/3600
    statusproc3=statusproc3*100
    return statusproc3

def statush_proch4():
    statusproc4=statush4()
    statusproc4=statusproc4/3600
    statusproc4=statusproc4*100
    return statusproc4

def statush_proch5():
    statusproc5=statush5()
    statusproc5=statusproc5/3600
    statusproc5=statusproc5*100
    return statusproc5

def statush_proch6():
    statusproc6=statush6()
    statusproc6=statusproc6/3600
    statusproc6=statusproc6*100
    return statusproc6


def statusd_proc1():
    statusproc1=statusd1()
    statusproc1=statusproc1/86400
    statusproc1=statusproc1*100
    return statusproc1
def statusd_proc2():
    statusproc2=statusd2()
    statusproc2=statusproc2/86400
    statusproc2=statusproc2*100
    return statusproc2
def statusd_proc3():
    statusproc3=statusd3()
    statusproc3=statusproc3/86400
    statusproc3=statusproc3*100
    return statusproc3
def statusd_proc4():
    statusproc4=statusd4()
    statusproc4=statusproc4/86400
    statusproc4=statusproc4*100
    return statusproc4
def statusd_proc5():
    statusproc5=statusd5()
    statusproc5=statusproc5/86400
    statusproc5=statusproc5*100
    return statusproc5
def statusd_proc6():
    statusproc6=statusd6()
    statusproc6=statusproc6/86400
    statusproc6=statusproc6*100
    return statusproc6

def statusd1():
    statusd=0
    if currentwork1_1()==1:
        statusd=status_d1()
    if currentwork1_1()==0:
        statusd=status_d1_0()
    if currentwork1_1()==2:
        statusd=status_d1_2()
    if currentwork1_1()==3:
        statusd=status_d1_3()
    return statusd
def statusd2():
    if currentwork2_2()==1:
        statusd=status_d2()
    if currentwork2_2()==0:
        statusd=status_d2_0()
    if currentwork2_2()==2:
        statusd=status_d2_2()
    if currentwork2_2()==3:
        statusd=status_d2_3()
    return statusd
def statusd3():
    if currentwork3_3()==1:
        statusd=status_d3()
    if currentwork3_3()==0:
        statusd=status_d3_0()
    if currentwork3_3()==2:
        statusd=status_d3_2()
    if currentwork3_3()==3:
        statusd=status_d3_3()
    return statusd
def statusd4():
    if currentwork4_4()==1:
        statusd=status_d4()
    if currentwork4_4()==0:
        statusd=status_d4_0()
    if currentwork4_4()==2:
        statusd=status_d4_2()
    if currentwork4_4()==3:
        statusd=status_d4_3()
    return statusd
def statusd5():
    if currentwork5_5()==1:
        statusd=status_d5()
    if currentwork5_5()==0:
        statusd=status_d5_0()
    if currentwork5_5()==2:
        statusd=status_d5_2()
    if currentwork5_5()==3:
        statusd=status_d5_3()
    return statusd
def statusd6():
    if currentwork6_6()==1:
        statusd=status_d6()
    if currentwork6_6()==0:
        statusd=status_d6_0()
    if currentwork6_6()==2:
        statusd=status_d6_2()
    if currentwork6_6()==3:
        statusd=status_d6_3()
    return statusd
def status_d1():
    data=readalldata()
    statusd=data[0]['status_d'][1]
    return  statusd
def status_d2():
    data=readalldata()
    statusd=data[1]['status_d'][1]
    return  statusd
def status_d3():
    data=readalldata()
    statusd=data[2]['status_d'][1]
    return  statusd
def status_d4():
    data=readalldata()
    statusd=data[3]['status_d'][1]
    return  statusd
def status_d5():
    data=readalldata()
    statusd=data[4]['status_d'][1]
    return  statusd
def status_d6():
    data=readalldata()
    statusd=data[5]['status_d'][1]
    return  statusd
def status_d1_0():
    data=readalldata()
    statusd=data[0]['status_d'][0]
    return  statusd
def status_d2_0():
    data=readalldata()
    statusd=data[1]['status_d'][0]
    return  statusd
def status_d3_0():
    data=readalldata()
    statusd=data[2]['status_d'][0]
    return  statusd
def status_d4_0():
    data=readalldata()
    statusd=data[3]['status_d'][0]
    return  statusd
def status_d5_0():
    data=readalldata()
    statusd=data[4]['status_d'][0]
    return  statusd
def status_d6_0():
    data=readalldata()
    statusd=data[5]['status_d'][0]
    return  statusd
def status_d1_2():
    data=readalldata()
    statusd=data[0]['status_d'][2]
    return  statusd
def status_d2_2():
    data=readalldata()
    statusd=data[1]['status_d'][2]
    return  statusd
def status_d3_2():
    data=readalldata()
    statusd=data[2]['status_d'][2]
    return  statusd
def status_d4_2():
    data=readalldata()
    statusd=data[3]['status_d'][2]
    return  statusd
def status_d5_2():
    data=readalldata()
    statusd=data[4]['status_d'][2]
    return  statusd
def status_d6_2():
    data=readalldata()
    statusd=data[5]['status_d'][2]
    return  statusd
def status_d1_3():
    data=readalldata()
    statusd=data[0]['status_d'][3]
    return  statusd
def status_d2_3():
    data=readalldata()
    statusd=data[1]['status_d'][3]
    return  statusd
def status_d3_3():
    data=readalldata()
    statusd=data[2]['status_d'][3]
    return  statusd
def status_d4_3():
    data=readalldata()
    statusd=data[3]['status_d'][3]
    return  statusd
def status_d5_3():
    data=readalldata()
    statusd=data[4]['status_d'][3]
    return  statusd
def status_d6_3():
    data=readalldata()
    statusd=data[5]['status_d'][3]
    return  statusd
def load_h1():
    data=readalldata()
    load=data[0]['load_h'][1]
    load=load*100
    return  load
def load_h2():
    data=readalldata()
    load=data[1]['load_h'][1]
    load=load*100
    return  load
def load_h3():
    data=readalldata()
    load=data[2]['load_h'][1]
    load=load*100
    return  load
def load_h4():
    data=readalldata()
    load=data[3]['load_h'][1]
    load=load*100
    return  load
def load_h5():
    data=readalldata()
    load=data[4]['load_h'][1]
    load=load*100
    return  load
def load_h6():
    data=readalldata()
    load=data[5]['load_h'][1]
    load=load*100
    return  load
def load_d1():
    data=readalldata()
    load=data[0]['load_d'][1]
    load=load*100
    return  load
def load_d2():
    data=readalldata()
    load=data[1]['load_d'][1]
    load = load * 100
    return  load
def load_d3():
    data=readalldata()
    load=data[2]['load_d'][1]
    load = load * 100
    return  load
def load_d4():
    data=readalldata()
    load=data[3]['load_d'][1]
    load = load * 100
    return  load
def load_d5():
    data=readalldata()
    load=data[4]['load_d'][1]
    load = load * 100
    return  load
def load_d6():
    data=readalldata()
    load=data[5]['load_d'][1]
    load = load * 100
    return  load
def obrabotka1_():
    data=readalldata()
    obrabot=data[0]['count_d']
    return obrabot
def obrabotka2_():
    data=readalldata()
    obrabot=data[1]['count_d']
    return obrabot
def obrabotka3_():
    data=readalldata()
    obrabot=data[2]['count_d']
    return obrabot
def obrabotka4_():
    data=readalldata()
    obrabot=data[3]['count_d']
    return obrabot
def obrabotka5_():
    data=readalldata()
    obrabot=data[4]['count_d']
    return obrabot
def obrabotka6_():
    data=readalldata()
    obrabot=data[5]['count_d']
    return obrabot
def obrabotka1_h():
    data=readalldata()
    obrabot=data[0]['count_h']
    return obrabot
def obrabotka2_h():
    data=readalldata()
    obrabot=data[1]['count_h']
    return obrabot
def obrabotka3_h():
    data=readalldata()
    obrabot=data[2]['count_h']
    return obrabot
def obrabotka4_h():
    data=readalldata()
    obrabot=data[3]['count_h']
    return obrabot
def obrabotka5_h():
    data=readalldata()
    obrabot=data[4]['count_h']
    return obrabot
def obrabotka6_h():
    data=readalldata()
    obrabot=data[5]['count_h']
    return obrabot
def proc_brack():
    data = readalldata()
    y = data[1]['params'][0]['value']
    h = data[5]['params'][0]['value']
    g=(y/h)*100
    return g
def brack_():
    data=readalldata()
    z=data[1]['params'][0]['value']
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
def weit_status1_1():
    data=readalldata()
    c=0
    if data[0]['params'][2]['value'] == 0:
         c =0
    if data[0]['params'][2]['value'] == 1:
        c = 1
    if data[0]['params'][2]['value'] == 2:
        c = 2
    return c
def weit_status2_2():
    data=readalldata()
    c=0
    if data[1]['params'][2]['value'] == 0:
         c = 0
    if data[1]['params'][2]['value'] == 1:
        c = 1
    if data[1]['params'][2]['value'] == 2:
        c =2
    return c
def weit_status3_3():
    data=readalldata()
    c=0
    if data[2]['params'][2]['value'] == 0:
         c = 0
    if data[2]['params'][2]['value'] == 1:
        c = 1
    if data[2]['params'][2]['value'] == 2:
        c = 2
    return c
def weit_status4_4():
    data=readalldata()
    c=0
    if data[3]['params'][2]['value'] == 0:
         c = 0
    if data[3]['params'][2]['value'] == 1:
        c = 1
    if data[3]['params'][2]['value'] == 2:
        c = 2
    return c
def weit_status5_5():
    data=readalldata()
    c=0
    if data[4]['params'][2]['value'] == 0:
         c = 0
    if data[4]['params'][2]['value'] == 1:
        c = 1
    if data[4]['params'][2]['value'] == 2:
        c = 2
    return c
def weit_status6_6():
    data=readalldata()
    c=0
    if data[5]['params'][2]['value'] == 0:
         c = 0
    if data[5]['params'][2]['value'] == 1:
        c = 1
    if data[5]['params'][2]['value'] == 2:
        c = 2
    return c
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
def currentwork1_1():
    data=readalldata()
    c=0
    if data[0]['params'][1]['value'] == 0:
         c = 0
    if data[0]['params'][1]['value'] == 1:
        c = 1
    if data[0]['params'][1]['value'] == 2:
        c = 2
    if data[0]['params'][1]['value'] == 3:
         c = 3
    return c
def currentwork2_2():
    data=readalldata()
    c=0
    if data[1]['params'][1]['value'] == 0:
         c =0
    if data[1]['params'][1]['value'] == 1:
        c = 1
    if data[1]['params'][1]['value'] == 2:
        c = 2
    if data[1]['params'][1]['value'] == 3:
         c = 3
    return c
def currentwork3_3():
    data=readalldata()
    c=0
    if data[2]['params'][1]['value'] == 0:
         c = 0
    if data[2]['params'][1]['value'] == 1:
        c = 1
    if data[2]['params'][1]['value'] == 2:
        c = 2
    if data[2]['params'][1]['value'] == 3:
         c = 3
    return c
def currentwork4_4():
    data=readalldata()
    c=0
    if data[3]['params'][1]['value'] == 0:
         c = 0
    if data[3]['params'][1]['value'] == 1:
        c = 1
    if data[3]['params'][1]['value'] == 2:
        c = 2
    if data[3]['params'][1]['value'] == 3:
         c = 3
    return c
def currentwork5_5():
    data=readalldata()
    c=0
    if data[4]['params'][1]['value'] == 0:
         c = 0
    if data[4]['params'][1]['value'] == 1:
        c = 1
    if data[4]['params'][1]['value'] == 2:
        c = 2
    if data[4]['params'][1]['value'] == 3:
         c = 3
    return c
def currentwork6_6():
    data=readalldata()
    c=0
    if data[5]['params'][1]['value'] == 0:
         c = 0
    if data[5]['params'][1]['value'] == 1:
        c = 1
    if data[5]['params'][1]['value'] == 2:
        c = 2
    if data[5]['params'][1]['value'] == 3:
         c = 3
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
    obraot1=obrabotka1_()
    obraot2 = obrabotka2_()
    obraot3 = obrabotka3_()
    obraot4 = obrabotka4_()
    obraot5 = obrabotka5_()
    obraot6 = obrabotka6_()
    obrabotkah1=obrabotka1_h()
    obrabotkah2 = obrabotka2_h()
    obrabotkah3 = obrabotka3_h()
    obrabotkah4 = obrabotka4_h()
    obrabotkah5 = obrabotka5_h()
    obrabotkah6 = obrabotka6_h()
    loadh= (load_h1()+load_h2()+load_h3()+load_h4()+load_h5()+load_h6())/6
    brack=brack_()
    pusk=pusk6_()
    speed=speed_ln()
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
    loadd1 = load_d1()
    loadh1 = load_h1()
    loadd2 = load_d2()
    loadh2 = load_h2()
    loadd3 = load_d3()
    loadh3 = load_h3()
    loadd4 = load_d4()
    loadh4 = load_h4()
    loadd5 = load_d5()
    loadh5 = load_h5()
    loadd6 = load_d6()
    loadh6 = load_h6()
    return render_template('main.html',data=data,coutworcks=coutworcks,countcellunworcks=countcellunworcks,countcellweit=countcellweit,countcellerror=countcellerror,pusk=pusk,currentcount1=currentcount1,currentcount2=currentcount2,currentcount3=currentcount3,currentcount4=currentcount4,currentcount5=currentcount5,currentcount6=currentcount6,
                           weitstatus1 =weitstatus1,proc_brac=proc_brac ,weitstatus2 =weitstatus2,weitstatus3 =weitstatus3 ,weitstatus4 =weitstatus4 ,weitstatus5 =weitstatus5 ,weitstatus6 =weitstatus6,brack=brack,
                           obraot1=obraot1,obraot2=obraot2,obraot3=obraot3,obraot4=obraot4,obraot5=obraot5,obraot6=obraot6,
                           obrabotkah1=obrabotkah1,obrabotkah2=obrabotkah2,obrabotkah3=obrabotkah3,obrabotkah4=obrabotkah4,obrabotkah5=obrabotkah5,obrabotkah6=obrabotkah6,
                           loadh=loadh,speed=speed,loadd1=loadd1,loadh1=loadh1,loadd2=loadd2,loadh2=loadh2 ,loadd3=loadd3,loadh3=loadh3
                           ,loadd4=loadd4,loadh4=loadh4 ,loadd5=loadd5,loadh5=loadh5 ,loadd6=loadd6,loadh6=loadh6 )




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
    obrabotkah1 = obrabotka1_h()
    obraot1 = obrabotka1_()
    load_d=load_d1()
    load_h=load_h1()
    statusprocd=statusd_proc1()
    currentcount=currentwork1()
    coutworcks = countcellworcks()
    countcellunworcks = unworcks_cell()
    countcellweit = weit_countcell()
    countcellerror = error_countcell()
    weitstatus = weit_status1()
    statusd=statusd1()
    statush = statush1()
    wtstushd=wstatush1()
    wtatusd=weitstatus1()
    statusproch=statush_proch1()
    wstatusdproc=wstatusd_proc1()
    wstatushproch= wstatush_proch1()

    return render_template('cell1.html', data=data, coutworcks=coutworcks, countcellunworcks=countcellunworcks,
                           countcellweit=countcellweit, countcellerror=countcellerror,currentcount=currentcount, weitstatus=weitstatus,pusk=pusk,obrabotkah1=obrabotkah1,
                           obraot1= obraot1,load_d=load_d,load_h=load_h, statusd=statusd,statusproc=statusprocd,statush=statush,statusproch=statusproch,
                           wstatusdproc=wstatusdproc,wstatushproch=wstatushproch,wtstushd=wtstushd,wtatusd=wtatusd)


@app.route("/cell2")
def mon_2():
    data = readdata()
    pusk=pusk2_()
    obraot2 = obrabotka2_()
    obrabotkah2 = obrabotka2_h()
    load_d = load_d2()
    load_h = load_h2()
    statusprocd = statusd_proc2()
    currentcount = currentwork2()
    coutworcks = countcellworcks()
    countcellunworcks = unworcks_cell()
    countcellweit = weit_countcell()
    countcellerror = error_countcell()
    weitstatus = weit_status2()
    statusd=statusd2()
    statusproch = statush_proch2()
    statush = statush2()
    wstatusdproc = wstatusd_proc2()
    wstatushproch= wstatush_proch2()
    wtstushd = wstatush2()
    wtatusd = weitstatus2()
    return render_template('cell2.html', data=data, coutworcks=coutworcks, countcellunworcks=countcellunworcks,
                           countcellweit=countcellweit, countcellerror=countcellerror,currentcount=currentcount,weitstatus=weitstatus,pusk=pusk,obraot2=obraot2,
                           obrabotkah2=obrabotkah2,load_d=load_d,load_h=load_h, statusd= statusd,statusproc=statusprocd,statush=statush,statusproch=statusproch
                           ,wstatusdproc=wstatusdproc,wstatushproch=wstatushproch,wtstushd=wtstushd,wtatusd=wtatusd)


@app.route("/cell3")
def mon_3():
    data = readdata()
    pusk=pusk3_()
    obraot3 = obrabotka3_()
    obrabotkah3 = obrabotka3_h()
    load_d = load_d3()
    load_h = load_h3()
    statusprocd = statusd_proc3()
    wstatusdproc = wstatusd_proc3()
    wstatushproch= wstatush_proch3()
    wtstushd = wstatush3()
    wtatusd = weitstatus3()
    currentcount = currentwork3()
    coutworcks = countcellworcks()
    countcellunworcks = unworcks_cell()
    countcellweit = weit_countcell()
    countcellerror = error_countcell()
    weitstatus = weit_status3()
    statusd = statusd3()
    statusproch = statush_proch3()
    statush = statush3()
    return render_template('cell3.html', data=data, coutworcks=coutworcks, countcellunworcks=countcellunworcks,
                           countcellweit=countcellweit, countcellerror=countcellerror,currentcount=currentcount,weitstatus=weitstatus,pusk=pusk,obraot3=obraot3,
                           obrabotkah3= obrabotkah3,load_d=load_d ,load_h=load_h, statusd= statusd,statusproc=statusprocd,statush=statush,statusproch=statusproch
                           ,wstatusdproc=wstatusdproc,wstatushproch=wstatushproch,wtstushd=wtstushd,wtatusd=wtatusd)


@app.route("/cell4")
def mon_4():
    data = readdata()
    pusk=pusk4_()
    obraot4 = obrabotka4_()
    obrabotkah4 = obrabotka4_h()
    load_d= load_d4()
    load_h = load_h4()
    statusprocd = statusd_proc4()
    wstatusdproc = wstatusd_proc4()
    wstatushproch= wstatush_proch4()
    wtstushd = wstatush4()
    wtatusd = weitstatus4()
    coutworcks = countcellworcks()
    currentcount = currentwork4()
    countcellunworcks = unworcks_cell()
    countcellweit = weit_countcell()
    countcellerror = error_countcell()
    weitstatus = weit_status4()
    statusd=statusd4()
    statusproch = statush_proch4()
    statush = statush4()
    return render_template('cell4.html', data=data, coutworcks=coutworcks, countcellunworcks=countcellunworcks,
                           countcellweit=countcellweit, countcellerror=countcellerror,currentcount=currentcount,weitstatus=weitstatus,pusk=pusk, obraot4 = obraot4 ,
                           obrabotkah4= obrabotkah4,load_d=load_d,load_h=load_h, statusd= statusd,statusproc=statusprocd,statush=statush,statusproch=statusproch
                           ,wstatusdproc=wstatusdproc,wstatushproch=wstatushproch,wtstushd=wtstushd,wtatusd=wtatusd)


@app.route("/cell5")
def mon_5():
    data = readdata()
    coutworcks = countcellworcks()
    pusk=pusk5_()
    obraot5 = obrabotka5_()
    obrabotkah5 = obrabotka5_h()
    load_d = load_d5()
    load_h = load_h5()
    statusprocd = statusd_proc5()
    statusproch = statush_proch5()
    currentcount = currentwork5()
    countcellunworcks = unworcks_cell()
    countcellweit = weit_countcell()
    countcellerror = error_countcell()
    weitstatus = weit_status5()
    statusd=statusd5()
    wstatusdproc = wstatusd_proc5()
    wstatushproch= wstatush_proch5()
    wtstushd = wstatush5()
    wtatusd = weitstatus5()
    statush = statush5()
    return render_template('cell5.html', data=data, coutworcks=coutworcks, countcellunworcks=countcellunworcks,
                           countcellweit=countcellweit, countcellerror=countcellerror,currentcount=currentcount,weitstatus=weitstatus,pusk=pusk, obraot5= obraot5,
                           obrabotkah5=obrabotkah5,load_d=load_d,load_h=load_h, statusd= statusd,statusproc=statusprocd,statush=statush,statusproch=statusproch
                           ,wstatusdproc=wstatusdproc,wstatushproch=wstatushproch,wtstushd=wtstushd,wtatusd=wtatusd)


@app.route("/cell6")
def mon_6():
    data = readdata()
    pusk=pusk6_()
    obraot6 = obrabotka6_()
    obrabotkah6 = obrabotka6_h()
    load_d = load_d6()
    load_h = load_h6()
    statusprocd = statusd_proc6()
    statusproch = statush_proch6()
    coutworcks = countcellworcks()
    currentcount = currentwork6()
    countcellunworcks = unworcks_cell()
    countcellweit = weit_countcell()
    countcellerror = error_countcell()
    weitstatus = weit_status6()
    statusd=statusd6()
    wstatusdproc = wstatusd_proc6()
    wstatushproch= wstatush_proch6()
    wtstushd = wstatush6()
    wtatusd = weitstatus6()
    statush = statush6()
    return render_template('cell6.html', data=data, coutworcks=coutworcks, countcellunworcks=countcellunworcks,
                           countcellweit=countcellweit, countcellerror=countcellerror,currentcount=currentcount,weitstatus=weitstatus,pusk=pusk, obraot6 = obraot6 ,
                           obrabotkah6=obrabotkah6,load_d=load_d,load_h=load_h, statusd= statusd,statusproc=statusprocd,statush=statush,statusproch=statusproch
                           ,wstatusdproc=wstatusdproc,wstatushproch=wstatushproch,wtstushd=wtstushd,wtatusd=wtatusd)


@app.route("/mon_cell1")
def mon_7():
    data = readdata()
    obrabotkah1 = obrabotka1_h()
    obraot1 = obrabotka1_()
    load_d = load_d1()
    load_h = load_h1()

    currentcount = currentwork1()
    weitstatus = weit_status1()
    return render_template('mon_cell1.html', data=data, currentcount=currentcount, weitstatus=weitstatus,obraot1 =obraot1, obrabotkah1 = obrabotkah1
                           ,load_d=load_d,load_h=load_h,)
@app.route("/mon_cell2")
def mon_8():
    data = readdata()
    obraot2 = obrabotka2_()
    obrabotkah2 = obrabotka2_h()
    load_d = load_d2()
    load_h = load_h2()

    currentcount = currentwork2()
    weitstatus = weit_status2()
    return render_template('mon_cell2.html', data=data, currentcount=currentcount, weitstatus=weitstatus,obraot2 =obraot2,obrabotkah2=obrabotkah2
                           ,load_d=load_d,load_h=load_h)
@app.route("/mon_cell3")
def mon_9():
    data = readdata()
    obraot3 = obrabotka3_()
    obrabotkah3 = obrabotka3_h()
    load_d = load_d3()

    load_h = load_h3()
    currentcount = currentwork3()
    weitstatus = weit_status3()
    return render_template('mon_cell3.html', data=data, currentcount=currentcount, weitstatus=weitstatus,obraot3 =obraot3, obrabotkah3= obrabotkah3
                           ,load_d=load_d,load_h=load_h,)
@app.route("/mon_cell4")
def mon_10():
    data = readdata()
    obraot4 = obrabotka4_()
    obrabotkah4 = obrabotka4_h()
    load_d = load_d4()
    load_h = load_h4()

    currentcount = currentwork4()
    weitstatus = weit_status4()
    return render_template('mon_cell4.html', data=data, currentcount=currentcount, weitstatus=weitstatus,obraot4 =obraot4, obrabotkah4= obrabotkah4
                           ,load_d=load_d,load_h=load_h,)
@app.route("/mon_cell5")
def mon_11():
    data = readdata()
    obraot5 = obrabotka5_()
    obrabotkah5 = obrabotka5_h()
    load_d = load_d5()
    load_h = load_h5()

    currentcount = currentwork5()
    weitstatus = weit_status5()
    return render_template('mon_cell5.html', data=data, currentcount=currentcount, weitstatus=weitstatus,obraot5 =obraot5,obrabotkah5 =obrabotkah5
                           ,load_d=load_d,load_h=load_h,)
@app.route("/mon_cell6")
def mon_12():
   data = readdata()
   obraot6 = obrabotka6_()
   obrabotkah6 = obrabotka6_h()
   load_d = load_d6()
   load_h = load_h6()

   currentcount = currentwork6()
   weitstatus =weit_status6()
   return render_template('mon_cell6.html',data=data, currentcount=currentcount,weitstatus=weitstatus,obraot6 =obraot6, obrabotkah6= obrabotkah6
                          ,load_d=load_d,load_h=load_h,)

if __name__=="__main__":
    app.run(debug=True)