# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:04:06 2021

@author: gendutkiy
"""

import pymongo

class ConnectMongoDb():
    
    def __init__(self,host,port):
        self.server=host
        self.port=port
        self.param=f'mongodb://{self.server}:{self.port}/'
        try :
            self.conmongo=pymongo.MongoClient(self.param)
        except pymongo.errors.ServerSelectionTimeoutError as err: 
            self.conmongo=err
        
    def GetRespon(self):
        try :
            return self.conmongo.server_info().get('version')
        except pymongo.errors.ServerSelectionTimeoutError as err :
            return err
    
    
db_con=ConnectMongoDb('27.112.79.65', '27017')
print(type(db_con.GetRespon)