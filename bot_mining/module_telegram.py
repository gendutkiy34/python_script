# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 09:32:42 2021

@author: gendutkiy
"""

import requests
import datetime
import mysql.connector


def update_chat(token):
    param='https://api.telegram.org/{}/getupdates'.format(token)
    r=requests.get(param)
    respon=r.json()
    return respon

def send_chat(token,uid,msg):
    teletext='https://api.telegram.org/{}/sendMessage?chat_id={}&text={}'.format(token,uid,msg)
    requests.get(teletext) 
    #print(teletext)

def transaction_id(source):
    upd_id=(source['update_id'])
    return upd_id

def chatmsg(source):
    return source['message']['text']

def firstname(source):
    return source['message']['chat']['first_name']

def chatid(source):
    return source['message']['chat']['id']


def msg_contain(source):
    txt=source['text']
    return txt

def convert_date_unix(source):
    tmp=datetime.datetime.fromtimestamp(source['message']['date'])
    tgl=tmp.strftime('%Y-%m-%d %H:%M:%S')
    return tgl

def send_img(token,chat_id,pesan):
    param='https://api.telegram.org/{}/sendMessage?chat_id={}&text={}'.format(token,chat_id,pesan)
    request.post(param)



    
        