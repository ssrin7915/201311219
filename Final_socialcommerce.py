import urllib
from urlparse import urljoin
import codecs
from lxml import etree

f=codecs.open('coupang.txt','w','utf-8')
f.write('\n')

response=urllib.urlopen('http://www.coupang.com/np/categories/126?eventCategory=GNB2&eventLabel=local_KORSEO_total-KORSEO')
_html=response.read()
tree=etree.HTML(_html)
cn=0
_list1= tree.xpath('//*[@id="productList"]/li/a/strong/em/text()')
for _list in _list1:
    cn+=1 #print _list
    f.write(_list)
    f.write('\n')

tree2=etree.HTML(urllib.urlopen('http://www.coupang.com/np/categories/126?eventCategory=GNB2&eventLabel=local_KORSEO_total-KORSEO&page=2').read())
_list2= tree.xpath('//*[@id="productList"]/li/a/strong/em/text()')
for _list in _list2:
    cn+=1 #print _list
    f.write(_list)
    f.write('\n')
    
tree3=etree.HTML(urllib.urlopen('http://www.coupang.com/np/categories/126?eventCategory=GNB2&eventLabel=local_KORSEO_total-KORSEO&page=3').read())
_list3= tree.xpath('//*[@id="productList"]/li/a/strong/em/text()')
for _list in _list3:
    cn+=1
    f.write(_list)
    f.write('\n') #print _list

for i in range(1,56):
    url='http://www.coupang.com/np/search?q=%EC%9D%B4%EC%9A%A9%EA%B6%8C&channel=user&component=&eventCategory=SRP&sorter=&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&filterKey=&isPriceRange=false&brand=&rating=0&page='+str(i)
    #print url
    tree=etree.HTML(urllib.urlopen(url).read())
    _list=tree.xpath('//*[@id="productList"]/li/a/dl/dd/div[2]/text()')
    for x in _list:
        cn+=1
        f.write(x)
        f.write('\n')#print x
f.close()

import findspark
spark_home="C:\Users\our\Downloads\spark-1.6.0-bin-hadoop2.6"
findspark.init(spark_home)

import pyspark
conf=pyspark.SparkConf()
conf=pyspark.SparkConf().setAppName("myApp")
sc = pyspark.SparkContext(conf=conf)

from operator import add

lines = sc.textFile("coupang.txt")
wc = lines.flatMap(lambda x:x.split(' ')).map(lambda x:x.strip())
p =wc.collect()
count=sc.parallelize(p)\
         .map(lambda word: (word, 1))\
         .reduceByKey(add)\
         .sortBy(lambda a:a[1])\
         .collect()
for i in count:
    print i[0],":",i[1]
