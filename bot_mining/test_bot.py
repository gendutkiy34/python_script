open_file# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 12:11:54 2021

@author: gendutkiy
"""

import requests
import datetime
import mysql.connector
import module_telegram
#import module_general

token='1623472950:AAFbr-qVv3APa6M58EUUP7HkwZ8w4wZtXBU'
#dt = module_general.baca_file(r'C:\belajar\python\bot_mining\transaksi.txt')
#files=dt.read()
data=module_telegram.update_chat(token)

'''search & import update id'''
for src in data['result']:
    print(src)

''' check update id'''

#dt = module_general.baca_file(r'C:\belajar\python\test_beneran.txt')
#search_word = 'krahtt88'
#if(search_word in dt.read()):
#    print("ketemu")



        
            
