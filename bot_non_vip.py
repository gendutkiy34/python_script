#!/usr/bin/python3
from bot_mining import module_telegram as mt
from bot_mining import module_ethermine as me
from bot_mining import module_general as mg


token='bot1623472950:AAFbr-qVv3APa6M58EUUP7HkwZ8w4wZtXBU'
f=r'C:\belajar\python\bot_mining\transaksi.txt'
data_transaksi=mg.baca_file(f)
data_chat=mt.update_chat(token)

for tx in data_chat['result']:
    tx_id='{}\n'.format(tx['update_id'])
    msg=str.lower(mt.chatmsg(tx))
    fnm=mt.firstname(tx)
    ch_id=mt.chatid(tx)
    if tx_id in data_transaksi :
        pass
    else :
        if msg[0:4] == 'info' :
            pesan='hi {},\n- status-WalletId\n - Eth-diff'.format(fnm)
        elif msg[0:6] == 'status' :
            param=msg.split('-')
            wallet=param[1][0:43]
            param1=me.non_vip_data(wallet)
            pesan='hi {},\n\n{}'.format(fnm,param1)
        else :
            pesan='hi {},\nsilahkan ketik INFO'.format(fnm)
        mt.send_chat(token,ch_id,pesan)
        tambah_txid=mg.tambah_data(f)
        tambah_txid.write(tx_id)
        tambah_txid.close()
            
        

