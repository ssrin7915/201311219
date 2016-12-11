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
        [0,'my dog has flea problems. help please.'],
        [1,'maybe not take him to dog park stupid'],
        [0,'my dalmation is so cute. I love him'],
        [1,'stop posting stupid worthless garbage'],
        [0,'mr licks ate my steak how to stop him'],
        [1,'quit buying worthless dog food stupid'],
        [0,u'우리 강아지 벌레 있어요 도와주세요'],
        [0,u'우리 강아지 귀여워 너 사랑해'],
        [1,u'강아지 공원 가지마 바보같이'],
        [1,u'강아지 음식 구매 마세요 바보같이']
    ],
    ['cls','sent']
)
tokenizer = Tokenizer(inputCol="sent", outputCol="words")
tokDf = tokenizer.transform(df)
print tokDf.show()

from pyspark.ml.feature import StopWordsRemover
stop = StopWordsRemover(inputCol="words", outputCol="nostops")
stopDf=stop.transform(tokDf)
print stopDf.show()

from pyspark.ml.feature import CountVectorizer
cv = CountVectorizer(inputCol="nostops", outputCol="cv", vocabSize=30,minDF=1.0)
cvModel = cv.fit(stopDf)
cvDf = cvModel.transform(stopDf)

cvDf.collect()
print cvDf.select('words','nostops','cv').show()



