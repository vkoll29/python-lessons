# 1. Map - Reduce

# from mrjob.job import MRJob
# class MRSongCount(MRJob):
#     def mapper(self, _, song):
#         yield song, 1
#
#     def reducer(self, key, values):
#         yield (key, sum(values))
#
# if __name__ == "__main__":
#     MRSongCount.run()


## 2. READING AND WRITING FILES

import pyspark
from pyspark import SparkConf
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test Spark App").getOrCreate()
print(spark.sparkContext.getConf().getAll())
