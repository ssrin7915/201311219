import findspark
spark_home="C:\Users\media\Downloads\spark-1.6.0-bin-hadoop2.6"
findspark.init(spark_home)

import pyspark
conf=pyspark.SparkConf()
conf=pyspark.SparkConf().setAppName("myApp")
sc = pyspark.SparkContext(conf=conf)

from operator import add

lines = sc.textFile("SinhancardBenefit.txt")
wc = lines.flatMap(lambda x:x.split(' ')).map(lambda x:x.strip())
p =wc.collect()
count=sc.parallelize(p)\
         .map(lambda word: (word, 1))\
         .reduceByKey(add)\
         .sortBy(lambda a:a[1])\
         .collect()
for i in count:
    print i[0],":",i[1]

lines = sc.textFile("WooricardBenefit.txt")
wc = lines.flatMap(lambda x:x.split(' ')).map(lambda x:x.strip())
p =wc.collect()
count=sc.parallelize(p)\
         .map(lambda word: (word, 1))\
         .reduceByKey(add)\
         .sortBy(lambda a:a[1])\
         .collect()
for i in count:
    print i[0],":",i[1]
	
lines = sc.textFile("SamsungcardBenefit.txt")
wc = lines.flatMap(lambda x:x.split(' ')).map(lambda x:x.strip())
p =wc.collect()
count=sc.parallelize(p)\
         .map(lambda word: (word, 1))\
         .reduceByKey(add)\
         .sortBy(lambda a:a[1])\
         .collect()
for i in count:
    print i[0],":",i[1]