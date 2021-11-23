
#!/usr/bin/python3
import requests
import datetime



def update_chat(token):
    param='https://api.telegram.org/{}/getupdates'.format(token)
    r=requests.get(param)
    respon=r.json()
    return respon

def send_chat(token,uid,msg):
    teletext='https://api.telegram.org/{}/sendMessage?chat_id={}&text={}'.format(token,uid,msg)
    r=requests.get(teletext) 

def transaction_id(source):
    return str(source['update_id'])

def chatmsg(source):
    return source['message']['chat']

def firstname(source):
    return source['message']['chat']['first_name']

def chatid(source):
    return source['message']['chat']['id']

def msg_contain(source):
    return source['message']['text']


def convert_date_unix(source):
    tmp=datetime.datetime.fromtimestamp(source['message']['date'])
    tgl=tmp.strftime('%Y-%m-%d %H:%M:%S')
    return tgl





    
        
