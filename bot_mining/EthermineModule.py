# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 15:20:49 2021

@author: gendutkiy
"""

import requests
import datetime

def convert_date_unix(source):
    tmp=datetime.datetime.fromtimestamp(source)
    tgl=tmp.strftime('%Y-%m-%d')
    jm=tmp.strftime('%H:%M')
    return tgl,jm


'get dasboard current'
class GetDashboard:
    
    def __init__(self,wallet):
        self.wl_id=wallet
        try :
            param=f'https://api.ethermine.org/miner/{wallet}/dashboard'
            r=requests.get(param)
        except Exception :
            r={'data' : 'gagal ke API telegram'}
        self.respon=r.status_code
        self.data=r.json()
        self.list_tgl=[]
        self.list_rp=[]
        self.list_vs=[]
        
    def GetRespon(self):
        return self.respon
    
    def GetCurrentData(self):
        data_current={}
        for a in self.data['data']['currentStatistics'].items():
            if a[0] =='time' :
                data_current['date']=convert_date_unix(a[1])[0]
                data_current['time']=convert_date_unix(a[1])[1]
            elif a[0] =='reportedHashrate' :
                data_current['reportedHashrate']=round(a[1]/1000000,2)
            elif a[0] =='validShares' :
                data_current['validShares']=a[1]
            elif a[0] =='invalidShares' :
                data_current['invalidShares']=a[1]
            elif a[0] =='activeWorkers' :
                data_current['activeWorkers']=a[1]
            elif a[0] =='unpaid' :
                data_current['unpaid']=round(a[1]/1000000000000000000,5)
            else :
                pass
        data_current['wallet_id']=self.wl_id
        txt=f'''wallet_id   : {data_current['wallet_id']}\nReported Hashrate : {data_current['reportedHashrate']}\nActive Worker : {data_current['activeWorkers']}\nUnpaid Balance     : {data_current['unpaid']} ETH
        '''
        return txt