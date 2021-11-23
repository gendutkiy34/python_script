# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 13:40:22 2021

@author: gendutkiy
"""
import requests


def retrieve_data(url):
    param=url
    try :
        r=requests.get(param) 
        data=r.json()
    except Exception :
        data=''
    return data

def PrintData(data):
    print(data)

def check_data(data):
    if (isinstance(data, list)):
        return isinstance(data, list)
        
def ExportToFile(**kwargs):
    
    with open(filename,'a') as outfile :
        txt=f'{data},'
        outfile.write(txt)
        
        
def RetrieveExportData(**kwargs):
    
    try :
        r=requests.get(kwargs['url']) 
        data=r.json()
    except Exception :
        data=''
    
    
    with open(kwargs['filepath'],'a') as outfile :
        for dt in data :
            print(dt)
            txt=f'{data},'
            outfile.write(txt)
        outfile.close()
        
    

#url='https://jsonplaceholder.typicode.com/todos'
#fileku='sssssss.txt'
source={'url' : 'https://jsonplaceholder.typicode.com/todos','filepath' :'yyyyy.txt'}
RetrieveExportData(**source)

#url=”https://jsonplaceholder.typicode.com/todos”
#data_raw=retrieve_data(url)
#ExportToFile(data_raw)
#for dt in data_raw:
#    PrintData(dt)
#    ExportToFile('data' = dt,'filename' = fileku)
#
#import pprint
#p = pprint.PrettyPrinter(indent=2)
#with open(fileku,'r') as outfile :
#        for a in outfile :
#            print(a)
#            #pp.pprint(a)
            