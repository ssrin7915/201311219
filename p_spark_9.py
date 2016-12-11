import findspark
spark_home="C:\Users\media\Downloads\spark-1.6.0-bin-hadoop2.6"
findspark.init(spark_home)

import pyspark
conf=pyspark.SparkConf()
conf=pyspark.SparkConf().setAppName("myApp")
sc = pyspark.SparkContext(conf=conf)


from pyspark.sql import SQLContext
sqlCtx=SQLContext(sc)

df = sqlCtx.createDataFrame(
    [
        ['No','young', 'false', 'false', 'fair'],
        ['No','young', 'false', 'false', 'good'],
        ['Yes','young', 'true', 'false', 'good'],
        ['Yes','young', 'true', 'true', 'fair'],
        ['No','young', 'false', 'false', 'fair'],
        ['No','middle', 'false', 'false', 'fair'],
        ['No','middle', 'false', 'false', 'good'],
        ['Yes','middle', 'true', 'true', 'good'],
        ['Yes','middle', 'false', 'true', 'excellent'],
        ['Yes','middle', 'false', 'true', 'excellent'],
        ['Yes','old', 'false', 'true', 'excellent'],
        ['Yes','old', 'false', 'true', 'good'],
        ['Yes','old', 'true', 'false', 'good'],
        ['Yes','old', 'true', 'false', 'excellent'],
        ['No','old', 'false', 'false', 'fair'],
    ],
    ['cls','age','f1','f2','f3']
)

from pyspark.ml.feature import StringIndexer

labelIndexer = StringIndexer(inputCol="cls",outputCol="lables")
model = labelIndexer.fit(df)
df1=model.transform(df)

labelIndexer = StringIndexer(inputCol="age",outputCol="att_a")
model = labelIndexer.fit(df1)
df2=model.transform(df1)

labelIndexer = StringIndexer(inputCol="f1",outputCol="att_f1")
model = labelIndexer.fit(df2)
df3=model.transform(df2)

labelIndexer = StringIndexer(inputCol="f2",outputCol="att_f2")
model = labelIndexer.fit(df3)
df4=model.transform(df3)

labelIndexer = StringIndexer(inputCol="f3",outputCol="att_f3")
model = labelIndexer.fit(df4)
df5=model.transform(df4)

from pyspark.mllib.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

va = VectorAssembler(inputCols=["att_a","att_f1","att_f2","att_f3"],outputCol="features")
df6 = va.transform(df5)

df7=df6.withColumnRenamed('lables','label')
trainDf=df7.select('label','features')
trainDf.printSchema()
print trainDf.show()

from pyspark.mllib.regression import LabeledPoint
trainRdd = trainDf.map(lambda row: LabeledPoint(row.label,row.features))
print trainRdd.take(20)

from pyspark.ml.classification import LogisticRegression
lr = LogisticRegression(maxIter=10, regParam=0.01)
model1 = lr.fit(trainDf)
print model1.coefficients
print model1.intercept

from pyspark.sql import Row
test0 = sc.parallelize([Row(features=Vectors.dense(2,0,0,1))]).toDF()
result = model1.transform(test0).head()
print result.prediction
