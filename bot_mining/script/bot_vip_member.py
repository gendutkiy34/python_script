#!/usr/bin/python3

from bot_mining import module_general as mg
from bot_mining import module_telegram as mt
from bot_mining import module_ethermine as me

bot='bot1623472950:AAFbr-qVv3APa6M58EUUP7HkwZ8w4wZtXBU'

f=r'/home/gendutkiy/log/list_vip_member.txt'
vip_member=mg.baca_file(f)

for dt in vip_member:
    vp=mg.split_vip(dt)
    ch_id=vp[0]
    wl_id=vp[1]
    data_eth=me.vip_data(wl_id)
    mt.send_chat(bot,ch_id,data_eth)
