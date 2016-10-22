import os
import urllib
import urlparse

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

SERVICE='ArpltnInforInqireSvc'
OPERATION_NAME='getMinuDustFrcstDspth'
param1=SERVICE+'/'+OPERATION_NAME

d=dict()
d['dataTerm']='month'
param2=urllib.urlencode(d)
params=param1+'?'+'serviceKey='+key['gokr']+'&'+param2

url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc'
myurl=urlparse.urljoin(url,params)


import requests
data=requests.get(myurl).text

import re
f=open('my.txt','w')
p=re.compile('<informCode>(.+?)</informCode>')
res=p.findall(data)
for item in res:
    print item
    f.write(item)
    f.write('\n')
f.close()