#!/usr/bin/python3

from bot_mining import module_general as mg
from bot_mining import module_telegram as mt
from bot_mining import module_ethermine as me
from contextlib import suppress

bot='bot1623472950:AAFbr-qVv3APa6M58EUUP7HkwZ8w4wZtXBU'
f=r'/home/gendutkiy/log/list_vip_member.txt'
vip_member=mg.baca_file(f)
for dt in vip_member:
    try :
        txt=""
        vp=mg.split_vip(dt)
        ch_id=vp[0]
        wl_id=vp[1]
        nme=vp[2]
        param='https://api.ethermine.org/miner/{}/payouts'.format(wl_id)
        dp=me.send_param(param)
        data_payout=dp['data']
        fle=r'/home/gendutkiy/log/{}.txt'.format(wl_id)
        fl_check=mg.check_file(fle)
        n1=len(data_payout)
        if n1 > 0 :
            if (fl_check):
                local_data=mg.baca_file(fle)
                n2=len(local_data)
                for pyo in data_payout[0:10]:
                    tgl=me.convert_date_unix(pyo['paidOn'])
                    koin=round(pyo['amount']/1000000000000000000,5)
                    txt='{},{}\n'.format(tgl,koin)
                    if txt in local_data:
                        pass
                    else:
                        pesan='hi {},\n\nTransfer amount : {} ETH success.\nPlease check your wallet !!\nwallet_id:\n{}\n\n-happy mining-'.format(nme,koin,wl_id)
                        mt.send_chat(bot,ch_id,pesan)
                        local_data.insert(0,txt)
                        tulis=mg.write_file(fle)
                        for pp in local_data :
                            tulis.write(pp)
                        tulis.close()
            else:
                isi=""
                for pyo in data_payout:
                    txt=""
                    tgl=me.convert_date_unix(pyo['paidOn'])
                    koin=round(pyo['amount']/1000000000000000000,5)
                    txt='{},{}\n'.format(tgl,koin)
                    isi='{}\n{}'.format(isi,txt)
                tulis=mg.write_file(fle)
                tulis.write(isi)
                tulis.close()
                tgl=me.convert_date_unix(data_payout[0]['paidOn'])
                koin=round(data_payout[0]['amount']/1000000000000000000,5)
                txt='{},{}\n'.format(tgl,koin)
                pesan='hi {},\n\nTransfer amount : {} ETH success.\nPlease check your wallet !!\nwallet_id:\n{}\n\n-happy mining-'.format(nme,koin,wl_id)
                mt.send_chat(bot,ch_id,pesan)
    except LookupError:
        pass
