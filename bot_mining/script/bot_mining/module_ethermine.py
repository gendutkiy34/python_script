#!/usr/bin/python3
import requests
import datetime



def get_current_stat(wallet):
    param='https://api.ethermine.org/miner/{}/currentStats'.format(wallet)
    current_data=send_param(param)
    return current_data

def timenow():
    nw=datetime.datetime.now()
    skr=nw.strftime('%d-%m-%Y %H:%M')
    return skr

def data_current(source):
    nw=datetime.datetime.now()
    a=nw.strftime('%d-%m-%Y %H:%M')
    txt='=========================================================\n\t\treport {}\n'.format(a)
    rp=hashrate(source['reportedHashrate'])
    cr=hashrate(source['currentHashrate'])
    ah=hashrate(source['averageHashrate'])
    aw=source['activeWorkers']
    vs=source['validShares']
    ivs=source['invalidShares']
    st=source['staleShares']
    tdu=unpaid_usd(source['usdPerMin'])
    param1='{}\nReported Hashrate\t\t : {}\nCurrent Hastrate\t\t : {}\nAverage Hashrate\t\t : {}\n'.format(txt,rp,cr,ah)
    param2='Active Worker\t\t\t : {}\nValid Share\t\t\t : {}\nInvalid Share\t\t\t : {}\nStale Share\t\t\t : {}\nUnpaid Balance Today\t\t : {}'.format(aw,vs,ivs,st,tdu)
    param='{}{}'.format(param1,param2)
    return param
    

def send_param(parameter):
    param=parameter
    r=requests.get(param)
    data=r.json()
    return data
    
def hashrate(source):
    a=round(source/1000000,1)
    return a


def unpaid_usd(source):
    nw=datetime.datetime.now()
    dd=int(nw.strftime('%d'))
    mm=int(nw.strftime('%m'))
    yy=int(nw.strftime('%Y'))
    hh=int(nw.strftime('%H'))
    mn=int(nw.strftime('%M'))
    ss=int(nw.strftime('%S'))
    time1=datetime.time(00, 00, 00)
    time2=datetime.time(hh, mn,ss)
    date=datetime.date(yy,mm,dd)
    datetime1=datetime.datetime.combine(date,time1)
    datetime2=datetime.datetime.combine(date,time2)
    delta=round(((datetime2-datetime1).total_seconds())/60)
    total=round(delta*source,2)
    return total

def get_worker(wallet):
    param='https://api.ethermine.org/miner/{}/workers'.format(wallet)
    worker=send_param(param)
    return worker

def data_worker(source):
    txt="==========================================================================\n\t\t\t\tData Worker\nworkername : report_hashrate , current_hasrate, valid_share, invalid_share\n"
    for w in source :
        wme=w['worker']
        rh=round(w['reportedHashrate']/1000000,1)
        cr=round(w['currentHashrate']/1000000,1)
        vs=w['validShares']
        ivs=w['invalidShares']
        param='{} : {} , {} , {} , {}'.format(wme,rh,cr,vs,ivs)
        txt='{}\n{}'.format(txt,param)
    return txt

def get_config(wallet):
    param='https://api.ethermine.org/miner/{}/settings'.format(wallet)
    config=send_param(param)
    return config

def data_config(source):
    txt="================================================================\n\t\t\tdata configuration\n"
    em=source['email']
    mp=round(source['minPayout']/1000000000000000000,2)
    gl=source['gasPriceLimit']
    ip=source['ip']
    param='{}\nemail\t\t\t: {}\nMinPayout\t\t: {}\ngasPriceLimit\t\t: {}'.format(txt,em,mp,gl)
    return param        
        
    

def vip_data(wallet):
    param='https://api.ethermine.org/miner/{}/currentStats'.format(wallet)
    current_data=send_param(param)
    param='https://api.ethermine.org/miner/{}/workers'.format(wallet)
    worker_data=send_param(param)
    jam=timenow()
    usd=usd_now()
    nd=""
    txt="======= {} =======\n\n".format(jam)
    ttl=0
    aw=current_data['data']['activeWorkers']
    vs=current_data['data']['validShares']
    ivs=current_data['data']['invalidShares']
    st=current_data['data']['staleShares']
    #tdu=unpaid_usd(current_data['data']['usdPerMin'])
    tdu=round((current_data['data']['unpaid']/1000000000000000000)*usd,2)
    esm=round(43200*current_data['data']['usdPerMin'],2)
    for dt in worker_data['data']:
        cr=round(dt['reportedHashrate']/1000000,1)
        nd='{}  |  {}'.format(str(cr),nd)
        ttl += round(cr,1)
    param1='Worker HastRate\t\t: {}\nTotal HastRate\t\t: {} Mhs\nActive Worker\t\t: {}\nUnpaid Balance\t: {} USD\nEstimate Earning Monthly\t: {} USD\n'.format(nd,round(ttl,1),aw,tdu,esm)
    param2='Valid Share\t\t: {}\nInvalid Share\t\t: {}\nStale Share\t\t: {}\n'.format(vs,ivs,st)
    txt='{}{}{}'.format(txt,param1,param2)
    return txt


def vip_alarm(wallet):
    param='https://api.ethermine.org/miner/{}/workers'.format(wallet)
    worker_data=send_param(param)
    nd=""
    jam=timenow()
    txt="====================================================================\n\t\t{}\n\tWARNING YOUR WORKER OFFLINE !!!\n".format(jam)
    jumlahnode=len(worker_data['data'])
    node_active=0
    for data in worker_data['data']:
        cr=round(data['currentHashrate']/1000000,1)
        if cr < 15 :
            nd ='{} '.format(data['worker'])
        else :
            node_active += 1
    if node_active < jumlahnode :
        allert='{}offline node :\n{}'.format(txt,nd)
        return allert
    
def node_offine(wallet):
    param='https://api.ethermine.org/miner/{}/workers'.format(wallet)
    worker_data=send_param(param)
    jumlahnode=len(worker_data['data'])
    active_node=len(worker_data['data'])
    for data in worker_data['data']:
        cr=round(data['currentHashrate']/1000000,1)
        if cr < 15 :
            active_node -= 1
        if active_node < jumlahnode :
            txt='node_offline'
            return txt

def non_vip_data(wallet):
    param='https://api.ethermine.org/miner/{}/currentStats'.format(wallet)
    current_data=send_param(param)
    src=current_data['data']
    usd=usd_now()
    rh=round(src['reportedHashrate']/1000000,1)
    aw=src['activeWorkers']
    #tdu=unpaid_usd(src['usdPerMin'])
    tdu=round((src['unpaid']/1000000000000000000)*usd,2)
    param1='Wallet ID\t: {}\nReported HashRate\t: {} Mhs\nActive Worker\t: {}\nUnpaid Balance\t: {} USD'.format(wallet,rh,aw,tdu)
    return param1

def convert_date_unix(source):
    tmp=datetime.datetime.fromtimestamp(source)
    tgl=tmp.strftime('%Y-%m-%d')
    return tgl

def get_payout_his(wallet):
    param='https://api.ethermine.org/miner/{}/payouts'.format(wallet)
    payout_data=send_param(param)
    txt=""
    if len(payout_data['data']) > 0:
        for dt in payout_data['data'][0:7]:
            tgl_payout=convert_date_unix(dt['paidOn'])
            jmlh_koin=round(dt['amount']/1000000000000000000,4)
            txt='{}\n{} : {} ETH'.format(txt,tgl_payout,jmlh_koin)
    else :
        txt='no payment history yet'
    return txt

def block_eth():
    src=send_param('https://api.ethermine.org/networkStats')
    data_block=src['data']
    return data_block

def diff_level():
    data=block_eth()
    diflevel=round(data['difficulty']/1000000000000000,1)
    return diflevel

def usd_now():
    data=block_eth()
    prc=round(data['usd'],2)
    return prc

def all_payout_his(wallet):
    param='https://api.ethermine.org/miner/{}/payouts'.format(wallet)
    payout_data=send_param(param)
    ls_pyaout=[]
    if len(payout_data['data']) > 0:
        for dt in payout_data['data']:
            ls_temp=[]
            tgl_payout=convert_date_unix(dt['paidOn'])
            ls_temp.append(tgl_payout)
            jmlh_koin=round(dt['amount']/1000000000000000000,4)
            ls_temp.append(jmlh_koin)
            ls_pyaout.append(ls_temp)
    else :
        pass
    return ls_pyaout
        
        
    
    

        

    


