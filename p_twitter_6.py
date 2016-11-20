import oauth2
import os
import urllib
import json

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

consumer = oauth2.Consumer(key=key['api_key'], secret=key['api_secret'])
token=oauth2.Token(key=key['access_token'], secret=key['access_secret'])
client = oauth2.Client(consumer,token)

_url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
url = "https://api.twitter.com/1.1/followers/list.json"

response, content = client.request(url, method="GET")
tfollower_json = json.loads(content)

for i in tfollower_json['users']:
    myparam={'screen_name':i['screen_name']}
    mybody=urllib.urlencode(myparam)
    _response, _content = client.request(_url+"?"+mybody, method="GET")
    tfollower_timeline = json.loads(_content)
    for j in  tfollower_timeline:
        print j['id'],j['text']