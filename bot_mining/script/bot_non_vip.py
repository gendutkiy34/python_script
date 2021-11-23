#!/usr/bin/python3
from bot_mining import module_telegram as mt
from bot_mining import module_ethermine as me
from bot_mining import module_general as mg
from contextlib import suppress

token='bot1623472950:AAFbr-qVv3APa6M58EUUP7HkwZ8w4wZtXBU'
f=r'/home/gendutkiy/script/transaksi.txt'
data_transaksi=mg.baca_file(f)
data_chat=mt.update_chat(token)

with suppress(Exception):
    for tx in data_chat['result']:
        tx_id='{}\n'.format(tx['update_id'])
        if 'text' in tx['message']:
            msg=mt.msg_contain(tx)
        else:
             tambah_txid=mg.tambah_data(f)
             tambah_txid.write(tx_id)
             tambah_txid.close()
        fnm=mt.firstname(tx)
        ch_id=mt.chatid(tx)
        if tx_id in data_transaksi :
            pass
        else:
            triger=msg.lower()
            if triger[0:4] == 'help':
                pesan='Hi {},\n\nplease following format as below:\n- STATUS-WalletID\n- DIFF-NOW\n- PAYOUT-WalletID\n\n-happy mining-\n\nsource:www.ethermine.org'.format(fnm)
            elif triger[0:5] == 'diff-':
                diflevel=me.diff_level()
                pesan='Hi {},\n\nDifficulty level at this time : {}\n\n-happy mining-\n\nsource:www.ethermine.org'.format(fnm,diflevel)
            elif triger[0:6] == 'status':
                param=msg.split('-')
                wl_id=param[1][0:43]
                txt=me.non_vip_data(wl_id)
                pesan='Hi {},\n\n{}\n\n-happy mining-\n\nsource:www.ethermine.org'.format(fnm,txt)
            elif triger[0:6] == 'payout':
                param=msg.split('-')
                wl_id=param[1][0:43]
                txt=me.get_payout_his(wl_id)
                pesan='Hi {},\n\nYour Payment History as below :\n{}\n\n-happy mining-\n\nsource:www.ethermine.org'.format(fnm,txt)
            else :
                pesan='Hi {},\n\nplease type : help\n\n-happy mining-\n\nsource:www.ethermine.org'.format(fnm)
            mt.send_chat(token,ch_id,pesan)
            tambah_txid=mg.tambah_data(f)
            tambah_txid.write(tx_id)
            tambah_txid.close()

