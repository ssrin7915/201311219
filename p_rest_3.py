import os

KEY = "476641415973736131303175436b506f"
TYPE = 'json'
SERVICE = 'SearchSTNBySubwayLineService'
START_INDEX='1'
END_INDEX='10'
LINE_NUM='1'
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
url+=LINE_NUM
import requests
data =requests.get(url)
print data.text