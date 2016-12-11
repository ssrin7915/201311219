import findspark
spark_home="C:\Users\our\Downloads\spark-1.6.0-bin-hadoop2.6"
findspark.init(spark_home)

import pyspark
conf=pyspark.SparkConf()
conf=pyspark.SparkConf().setAppName("myApp")
sc = pyspark.SparkContext(conf=conf)

import oauth2
import os
import urllib
import json
import codecs

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

f=codecs.open('twitter.txt','w','utf-8')
url = "https://api.twitter.com/1.1/search/tweets.json"
max_id = '805940231664848896'
for i in range(0,1000):
    myparam={'q':'ÄíÆù','count':100,'max_id': max_id}
    mybody=urllib.urlencode(myparam)
    response, content = client.request(url+"?"+mybody, method="GET")
    tsearch_json=json.loads(content)
    for tweet in tsearch_json['statuses']:
        cn += 1
        f.write(tweet['text'])
        f.write("\n")
    max_id = tsearch_json['statuses'][-1]['id']-1
f.close()

f=codecs.open('twitter2.txt','w','utf-8')
url = "https://api.twitter.com/1.1/search/tweets.json"
max_id = '804964333822148607'
for i in range(0,1000):
    myparam={'q':'ÄíÆù','count':100,'max_id': max_id}
    mybody=urllib.urlencode(myparam)
    response, content = client.request(url+"?"+mybody, method="GET")
    tsearch_json=json.loads(content)
    for tweet in tsearch_json['statuses']:
        f.write(tweet['text'])
        f.write("\n")
    max_id = tsearch_json['statuses'][-1]['id']-1
f.close()

from operator import add

lines = sc.textFile("twitter.txt")
wc = lines.flatMap(lambda x:x.split(' ')).map(lambda x:x.strip())
p =wc.collect()
count=sc.parallelize(p)\
         .map(lambda word: (word, 1))\
         .reduceByKey(add)\
         .sortBy(lambda a:a[1])\
         .collect()

for i in count:
    print i[0],":",i[1]

lines = sc.textFile("twitter2.txt")
wc = lines.flatMap(lambda x:x.split(' ')).map(lambda x:x.strip())
p =wc.collect()
count=sc.parallelize(p)\
         .map(lambda word: (word, 1))\
         .reduceByKey(add)\
         .sortBy(lambda a:a[1])\
         .collect()

for i in count:
    print i[0],":",i[1]
