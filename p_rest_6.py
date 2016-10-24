import os
import requests
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
USE_MON = '201306'


_maxIter=3
_iter=0
while _iter<_maxIter:
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
    response = requests.get(url).text
    print response
    START_INDEX= str(int(START_INDEX)+10)
    END_INDEX= str(int(END_INDEX)+10)
    _iter+=1