# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 10:13:11 2021

@author: gendutkiy
"""
import ethermine_module as em
import pprint
wallet_id='0xbe3d0ae733d04c72ce4e513e1200623576f8bdc5'
try :
    data_raw=em.GetDashboard(wallet_id)
except Exception:
    data_raw=[]
    

pprint.pprint(data_raw.GetCurrentData())


