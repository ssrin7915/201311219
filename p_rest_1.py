import requests
url='http://freegeoip.net/json/'
geostr=requests.get(url).text
print geostr

import json
geojson=json.loads(geostr)
print "Whatis IP Address?"
print geojson['ip']

country=geojson.get('country_code')
print "Whatis Country_Code?"
print country.decode('utf-8')

for k,v in geojson.iteritems():
    print k,"\t: ",v