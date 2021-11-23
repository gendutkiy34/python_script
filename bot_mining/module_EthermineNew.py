# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 12:29:39 2021

@author: gendutkiy
"""

import requests
import datetime

def convert_date_unix(source):
    tmp=datetime.datetime.fromtimestamp(source)
    tgl=tmp.strftime('%Y-%m-%d %H:%M')
    return tgl


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
        
    def get_Respon(self):
        return self.respon
    
    def get_DataHistory(self):
        for dt in self.data['data']['statistics']:
            tm=convert_date_unix(dt.get('reportedHashrate'))
            rp=round(dt.get('reportedHashrate')/1000000,1)
            vs=dt.get('validShares')
            self.list_tgl.append(tm)
            self.list_rp.append(rp)
            self.list_vs.append(vs)
        return self.list_tgl,self.list_rp,self.list_vs

class GetPayout(GetDashboard):
    
    def get_PayoutHis(self):
        param=f'https://api.ethermine.org/miner/{self.wl_id}/payouts'
        r=requests.get(param)
        self.data_payout=r.json()
        self.list_payout=[]
        self.list_paidon=[]
        for dt in self.data_payout['data']:
            pdo=convert_date_unix(dt.get('paidOn'))
            amo=round(dt.get('amount')/1000000000000000000,5)
            self.list_paidon.append(pdo)
            self.list_payout.append(amo)
        self.list_paidon.reverse()
        self.list_payout.reverse()
        return self.list_paidon,self.list_payout

class GetCurrentStat(GetDashboard):
    
    def get_CurrentStat(self):
        param=f'https://api.ethermine.org/miner/{self.wl_id}/currentStats'
        r=requests.get(param)
        self.data_current=r.json()
        self.ctm=convert_date_unix(self.data_current['data'].get('time'))
        self.crp=round(self.data_current['data'].get('reportedHashrate')/1000000,1)
        self.cup=round(self.data_current['data'].get('unpaid')/1000000000000000000,7)
        self.cvs=self.data_current['data'].get('validShares')
        self.cis=self.data_current['data'].get('invalidShares')
        self.cst=self.data_current['data'].get('staleShares')
        self.caw=self.data_current['data'].get('activeWorkers')
        self.cus=round(self.data_current['data'].get('usdPerMin'),5)
        return self.ctm,self.crp,self.cvs,self.cis,self.cst,self.caw,self.cus
    
class GetSetting(GetDashboard):
    
    def get_Config(self):
        param=f'https://api.ethermine.org/miner/{self.wl_id}/settings'
        r=requests.get(param)
        self.data_config=r.json()
        self.email=self.data_config['data'].get('email')
        self.minpay=round(self.data_config['data'].get('minPayout')/1000000000000000000,4)
        self.gaslim=self.data_config['data'].get('gasPriceLimit')
        return self.email,self.minpay,self.gaslim
    
class GetWorker(GetDashboard):
    
    def get_CurrentWorker(self):
         param=f'https://api.ethermine.org/miner/{self.wl_id}/workers'
         r=requests.get(param)
         self.data_worker=r.json()
         self.list_worker=[]
         for dt in self.data_worker['data']:
             txt=''
             tm=convert_date_unix(dt.get('time'))
             wk=dt.get('worker')
             rp=round(dt.get('reportedHashrate')/1000000,1)
             txt=f'{tm},{wk},{rp}'
             self.list_worker.append(txt)
         return self.list_worker






