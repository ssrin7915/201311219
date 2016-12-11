import findspark
spark_home="C:\Users\media\Downloads\spark-1.6.0-bin-hadoop2.6"
findspark.init(spark_home)

import pyspark
conf=pyspark.SparkConf()
conf=pyspark.SparkConf().setAppName("myApp")
sc = pyspark.SparkContext(conf=conf)


from pyspark.sql import SQLContext
from pyspark.sql.functions import rand, randn
sqlCtx=SQLContext(sc)

df = sqlCtx.range(0, 10)
df.select("id", rand(seed=10).alias("uniform"), randn(seed=27).alias("normal")).show()
print df.describe().show()

names = ["Alice", "Bob", "Mike"]
items = ["milk", "bread", "butter", "apples", "oranges"]
df = sqlCtx.createDataFrame([(names[i % 3], items[i % 5]) for i in range(100)], ["name", "item"])
print df.show(10)

df = sqlCtx.createDataFrame([(1, 2, 3) if i % 2 == 0 else (i, 2 * i, i % 4) for i in range(100)], ["a", "b", "c"])
print df.show(10)
