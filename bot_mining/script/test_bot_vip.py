#!/usr/bin/python3
from bot_mining import module_ethermine as me
from bot_mining import module_telegram as mt

#wallet_cepul='0xb85523805c316960e7fbc4518e23e0d3901dd1da'
#bot_RJC='bot1623472950:AAFbr-qVv3APa6M58EUUP7HkwZ8w4wZtXBU'
#id_cepul='2741313'
#isi=me.vip_data(wallet_cepul)
#mt.send_chat(bot_RJC,id_cepul,isi)

walletku='0x836bcc65ce8ebd3b7de3d85dd6afcf6921964fb3'
botku='bot1515311411:AAHeE5G6HfPGt9Wg4y1MNqG8MYvxIxgCbq8'
idku='697856611'
isiku=me.vip_data(walletku)
mt.send_chat(botku,idku,isiku)


