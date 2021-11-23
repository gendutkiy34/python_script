#!/usr/bin/python3

from bot_mining import module_general as mg
from bot_mining import module_telegram as mt
from bot_mining import module_ethermine as me
from contextlib import suppress


bot='bot1623472950:AAFbr-qVv3APa6M58EUUP7HkwZ8w4wZtXBU'

f=r'/home/gendutkiy/script/list_vip_member.txt'
vip_member=mg.baca_file(f)

with suppress(Exception):
    for dt in vip_member:
        vp=mg.split_vip(dt)
        ch_id=vp[0]
        wl_id=vp[1]
        data_payout=me.all_payout_his(wl_id)
        fl_vip=r'/home/gendutkiy/script/{}.txt'.format(wl_id)
        txt=""
        for dtp in data_payout:
            txt='{}\n{},{}'.format(txt,dtp[0],dtp[1])
        tambah_txid=mg.tambah_data(fl_vip)
        tambah_txid.write(txt)
        tambah_txid.close()
