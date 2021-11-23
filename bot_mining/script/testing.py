#!/usr/bin/python3

from bot_mining import module_general as mg
from bot_mining import module_telegram as mt
from bot_mining import module_ethermine as me

wallet='0xbe3d0ae733d04c72ce4e513e1200623576f8bdc5'
bot='bot1515311411:AAHeE5G6HfPGt9Wg4y1MNqG8MYvxIxgCbq8'
chatid='697856611'

nonvip_data=me.non_vip_data(wallet)
mt.send_chat(bot,chatid,nonvip_data)
