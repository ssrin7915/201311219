import os
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

KEY=key['dataseoul']
TYPE='xml'
SERVICE='CardSubwayStatisticsService'
START_INDEX='1'
END_INDEX='10'
USE_MON = '201512'

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

import requests
import lxml
import lxml.etree

data = requests.get(url).text
tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('row')
for node in nodes:
    s=node.xpath('SUB_STA_NM')
    r=node.xpath('RIDE_PASGR_NUM')
    print s[0].text , r[0].text