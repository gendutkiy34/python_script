#!/usr/bin/python3

from bot_mining import module_general as mg
from bot_mining import module_telegram as mt
from bot_mining import module_ethermine as me

f=r'/home/gendutkiy/log/list_vip_member.txt'
vip_member=mg.baca_file(f)

for dt in vip_member:
    vp=mg.split_vip(dt)
    wl_id=vp[1]
    param='https://api.ethermine.org/miner/{}/payouts'.format(wl_id)
    dp=me.send_param(param)
    data_payout=dp['data']
    txt=""
    fle=r'/home/gendutkiy/log/{}.txt'.format(wl_id)
    print(wl_id,':',len(data_payout))
    for dt in data_payout:
        tgl=me.convert_date_unix(dt['paidOn'])
        koin=round(dt['amount']/1000000000000000000,5)
        txt='{}{},{}\n'.format(txt,tgl,koin)
    tulis=mg.write_file(fle)
    tulis.write(txt)
    tulis.close()


''' tambaha manual 1 wallet '''
wl_id='0x836bcc65ce8ebd3b7de3d85dd6afcf6921964fb3'
param='https://api.ethermine.org/miner/{}/payouts'.format(wl_id)
dp=me.send_param(param)
data_payout=dp['data']
txt=""
fle=r'/home/gendutkiy/log/{}.txt'.format(wl_id)
for dt in data_payout:
    tgl=me.convert_date_unix(dt['paidOn'])
    koin=round(dt['amount']/1000000000000000000,5)
    txt='{}{},{}\n'.format(txt,tgl,koin)
tulis=mg.write_file(fle)
tulis.write(txt)
tulis.close()
