
import os
import findspark

spark_home = "C:\Users\media\Downloads\spark-1.6.0-bin-hadoop2.6"
findspark.init(spark_home)

import pyspark
from pyspark.sql import SQLContext
import requests

conf=pyspark.SparkConf()
conf=pyspark.SparkConf().setAppName("myApp")
sc = pyspark.SparkContext(conf=conf)
sqlCtx=SQLContext(sc)
r=requests.get("https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json")
wc=r.json()
wcDF=sqlCtx.createDataFrame(wc)
wcDF.registerTempTable("wc")
sqlCtx.sql("select Club,DateOfBirth,Number from wc").show()
sqlCtx.sql("select * from wc where Number=10").show()
