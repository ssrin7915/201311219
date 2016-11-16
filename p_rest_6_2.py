import os
import pymongo
from pymongo import MongoClient

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    lines=f.readlines()
    for line in lines:
        row=line.split('=')
        row0=row[0]
        d[row0] =row[1].strip()
    return d

keyPath=os.path.join(os.getcwd(),'src','key.properties')

key=getKey(keyPath)

client=MongoClient()
db=client.Api
col=db.subway

import lxml
import lxml.etree
import requests
import os

KEY=key['dataseoul']
TYPE='xml'
SERVICE='CardSubwayStatisticsService'

USE_MON = '201301'
START_INDEX='1'
END_INDEX='10'

for i in range(0,12):
    for y in range(0,3):
        url='http://openapi.seoul.go.kr:8088/'
        url+=KEY
        url+='/'
        url+=TYPE
        url+='/'
        url+=SERVICE
        url+='/'
        url+=START_INDEX
        url+='/'
        url+=END_INDEX
        url+='/'
        url+=USE_MON
        data=requests.get(url).text
        tree=lxml.etree.fromstring(data.encode('utf-8'))
        nodes=tree.xpath('row')
        for node in nodes:
            u=node.xpath('USE_MON')
            n=node.xpath('LINE_NUM')
            s=node.xpath('SUB_STA_NM')
            r=node.xpath('RIDE_PASGR_NUM')
            a=node.xpath('ALIGHT_PASGR_NUM')
            col.insert_one({
                "USE_MON" : u[0].text,
                "LINE_NUM" : n[0].text,
                "SUB_STA_NM" : s[0].text,
                "RIDE_PASGR_NUM" : r[0].text,
                "ALIGHT_PASGR_NUM" : a[0].text
            })
        START_INDEX= str(int(START_INDEX)+10)
        END_INDEX= str(int(END_INDEX)+10)
    USE_MON = str(int(USE_MON)+1)
        
empCol = col.find()
for emp in empCol:
    print emp