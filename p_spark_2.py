import os
import findspark

spark_home = "C:\Users\media\Downloads\spark-1.6.0-bin-hadoop2.6"
findspark.init(spark_home)

import pyspark

conf=pyspark.SparkConf()
conf=pyspark.SparkConf().setAppName("myApp")
sc = pyspark.SparkContext(conf=conf)

print sc._conf.getAll()