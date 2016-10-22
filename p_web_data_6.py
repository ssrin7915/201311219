# coding: cp949
import requests
import re

urlbase='http://www.kbreport.com/leader/main?'
url1='rows=20&order=oWAR&orderType=DESC&'
url2='teamId=1&defense_no=2&year_from=2015&year_to=2015&split01=&split02_1=&split02_2=&r_tpa_count=&tpa_count=0'
urlbaseball=urlbase+url1+url2

data=requests.get(urlbaseball).text
a=data.find('top-score-top')
b=data.find('top-score end')

mydata=data[a:b+len('top-score end')]

k=u'승'
p=re.compile('.'+k+'.+')
found=p.findall(mydata)

for item in found:
    print item