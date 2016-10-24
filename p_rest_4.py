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
SERVICE='ListLocaldata470401S'
START_INDEX='1'
END_INDEX='10'

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

import requests
data = requests.get(url).text

import re
p=re.compile('<STATMAN>(.+?)</STATMAN>')
res=p.findall(data)
for item in res:
    print item