#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 10:29:34 2021
@author: gendutkiy
this module purpose to parsing data from ethermine.org to NOSQL database
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
        param=f'https://api.ethermine.org/miner/{wallet}/dashboard'
        r=requests.get(param)
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
        return data_current


'get worker data current'
class GetWorker(GetDashboard):
    
    def GetCurrentWorker(self):
         param=f'https://api.ethermine.org/miner/{self.wl_id}/workers'
         r=requests.get(param)
         self.data_worker=r.json()
         worker_data=[]
         for wo in self.data_worker['data']:
             data_w={}
             for det in wo.items():
                 if det[0] == 'worker' :
                     data_w['name'] = det[1]
                 elif det[0] == 'time' :
                     data_w['date'] = convert_date_unix(det[1])[0]
                     data_w['time'] = convert_date_unix(det[1])[1]
                 elif det[0] == 'reportedHashrate' :
                     data_w['reportedHashrate'] = round(det[1]/1000000,2)
                 elif det[0] == 'validShares' :
                     data_w['validShares'] = det[1]
                 else :
                     pass
             data_w['wallet_id']=self.wl_id
             worker_data.append(data_w)
         return worker_data


'get payout data'     
class GetPayout(GetDashboard):
    
    def GetPayoutHis(self):
        param=f'https://api.ethermine.org/miner/{self.wl_id}/payouts'
        r=requests.get(param)
        self.data_payout=r.json()
        payout_data=[]
        for dp in self.data_payout['data']:
            d_pay={}
            for a in dp.items():
                if a[0] == 'paidOn':
                    d_pay['date']=convert_date_unix(a[1])[0]
                    d_pay['time']=convert_date_unix(a[1])[1]
                elif  a[0] == 'amount' :
                    d_pay['amount']=round(a[1]/1000000000000000000,5) 
                else :
                    pass
            d_pay['wallet_id']=self.wl_id
            payout_data.append(d_pay)
        return payout_data
         