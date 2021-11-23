#!/usr/bin/python3

from bot_mining import module_general as mg
from bot_mining import module_telegram as mt
from bot_mining import module_ethermine as me
from contextlib import suppress


wallet='0x836bcc65ce8ebd3b7de3d85dd6afcf6921964fb3'
bot_id='bot1515311411:AAHeE5G6HfPGt9Wg4y1MNqG8MYvxIxgCbq8'
chat_id='697856611'
param='https://api.ethermine.org/miner/{}/payouts'.format(wallet)
dp=me.send_param(param)
data_payout=dp['data']
fle=r'/home/gendutkiy/log/{}.txt'.format(wallet)
local_data=mg.baca_file(fle)

for pyo in data_payout[0:7]:
    try:
        txt=""
        tgl=me.convert_date_unix(pyo['paidOn'])
        koin=round(pyo['amount']/1000000000000000000,5)
        txt='{},{}\n'.format(tgl,koin)
        if txt in local_data:
            pass
        else:
            pesan='hi Gendutkiy,\n\nTransfer amount : {} ETH success.\nPlease check your wallet !!\nwallet_id:\n{}\n\n-happy mining-'.format(koin,wallet)
            mt.send_chat(bot_id,chat_id,pesan)
            local_data.insert(0,txt)
            tulis=mg.write_file(fle)
            for pp in local_data :
                tulis.write(pp)
            tulis.close()
    except LookupError:
        pass
