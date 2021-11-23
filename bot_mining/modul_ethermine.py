# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 09:33:32 2021

@author: gendutkiy
"""

import requests
import datetime



def get_current_stat(wallet):
    param='https://api.ethermine.org/miner/{}/currentStats'.format(wallet)
    r=requests.get(param)
    respon=r.json()
    return respon

def hashrate(source):
    a=round(source/1000000,1)
    return a
def unpaid_usd(source):
    nw=datetime.datetime.now()
    dd=int(nw.strftime('%d'))
    mm=int(nw.strftime('%m'))
    yy=int(nw.strftime('%Y'))
    hh=int(nw.strftime('%H'))
    mn=int(nw.strftime('%M'))
    ss=int(nw.strftime('%S'))
    time1=datetime.time(00, 00, 00)
    time2=datetime.time(hh, mn,ss)
    date=datetime.date(yy,mm,dd)
    datetime1=datetime.datetime.combine(date,time1)
    datetime2=datetime.datetime.combine(date,time2)
    delta=round(((datetime2-datetime1).total_seconds())/60)
    total=round(delta*source,2)
    return total

def get_worker(wallet):
    param='https://api.ethermine.org/miner/{}/currentStats'.format(workers)
    




