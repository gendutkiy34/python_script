#!/usr/bin/python3
import os
import matplotlib.pyplot as plt

def baca_file(source):
    dt=open(source,'r')
    data=dt.readlines()
    dt.close()
    return data

def tambah_data(source):
    data=open(source,'a')
    return data

def write_file(source) :
    data=open(source,'w')
    return data

def convert_date_unix(source):
    tmp=datetime.datetime.fromtimestamp(source)
    tgl=tmp.strftime('%Y-%m-%d %H:%M:%S')
    return tgl

def split_vip(source):
    data=source.split(';')
    return data

def check_file(files):
    fl=os.path.isfile(files)
    return fl

def export_graph(data_x,data_y,wallet,pth):
    plt.figure(figsize=(10,6))
    plt.bar(data_x,data_y)
    ttl='Payment History\nWallet ID : {}'.format(wallet)
    plt.title(ttl)
    plt.ylabel('num of coin')
    plt.xlabel('date')
    plt.savefig(pth,dpi=100)
    plt.close()
