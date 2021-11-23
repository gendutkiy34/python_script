# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 18:23:12 2021

@author: gendutkiy
"""
import requests
from scrapy import Selector
import pprint
import json

def GetDataUrl(url):
    res=requests.get(url)
    data=Selector(text=res.content)
    return data

def ExtracData(datahtml,tag=""):
    data_extract=datahtml.css(tag)
    return data_extract

def ExtractValue(datatag,tag=""):
    data_tag=datatag.css(tag).extract_first()
    return data_tag
page_url='https://cleantechnica.com/'
data_raw=GetDataUrl(page_url)
pg=1
data_scrap=[]
data_output=input('Masukkan path dan filename(.json) :')
for i in range(1,14):
    print (f'Grep Data {page_url}...')
    data_url=ExtracData(data_raw,tag='div.zox-art-title ')
    for x in data_url:
        judul=ExtractValue(x,tag='h2.zox-s-title2::text')
        url=ExtractValue(x,tag='a::attr(href)')
        data_arti=GetDataUrl(url)
        auth=ExtractValue(data_arti,tag='div.zox-author-name-wrap > span ::text')
        publ=ExtractValue(data_arti,tag='div.zox-post-date-wrap > span ::attr(datetime)')
        temp_art=ExtracData(data_arti,tag='div.zox-post-body > p')
        article=""
        for art in temp_art:
            if isinstance(ExtractValue(art,tag='::text'), str):
                article=article + ExtractValue(art,tag='::text')
        #article=" ".join(article)
        data ={'title' : judul,
               'publish' : publ,
               'content' : article,
               'author' : auth,
               'url' : url}
    data_scrap.append(data)
    pg += 1
    page_url=f'https://cleantechnica.com/page/{pg}/'
    data_raw=GetDataUrl(page_url)
print('grep data done.')
print(f'jumlah article : {len(data_scrap)}')
with open(data_output, "w") as file:
  file.write(json.dumps(data_scrap))
  
  

   