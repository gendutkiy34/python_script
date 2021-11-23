# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 17:18:46 2021

@author: gendutkiy
"""

import pandas as pd
import logging
import re

url='https://id.wikipedia.org/wiki/Daftar_miliarder_Forbes'

def getscrap(url):
    logging.info(f'grep data from {url}...')
    return pd.read_html(url,header=None)

def check_miliar(money_unit):
    return money_unit.lower().endswith('miliar')

def change_money_format(money_unit):
    half_clean = money_unit.lower().replace(",", ".").replace(" ", "")
    return re.sub(r"[?\[M\]miliar|\[J\]juta\|$]", "", half_clean)

def transform_data(df,tahun):
    logging.info('transform data starting ...')
    
    mapper={'No.':'no_urut',
            'Nama':'nama',
            'Kekayaan bersih (USD)':'kekayaan_bersih_USD',
            'Usia':'usia',
            'Kebangsaan':'kebangsaan',
            'Sumber kekayaan':'sumber_kekayaan'}
    rename_df=df.rename(columns=mapper)
    rename_df['tahun']='2018'
    rename_df['perusahaan']=rename_df['sumber_kekayaan']
    rename_df['kekayaan_bersih_USD']=rename_df['kekayaan_bersih_USD'].apply(
        lambda value: float(change_money_format(value))*1000 if check_miliar(value)
        else change_money_format(value))
    data_urut=[]
    a=1
    for i in range(len(rename_df['nama'])):
        data_urut.append(a)
        a +=1
    rename_df['no_urut']=data_urut
    return rename_df

source=getscrap(url)
data=source[1]
new_data=transform_data(data,2018)

