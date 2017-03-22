
"""Concatenate two dataframes in pyspark. 
   run as spark-submit concat_pyspark.py --py-files
"""

from __future__ import print_function
import pyspark
from pyspark import SparkContext
from pyspark.sql import SQLContext
logFile = "README.md"  # Should be some file on your system
sc = SparkContext("local", "pyspark")
sqlContext = SQLContext(sc)
logData = sc.textFile(logFile).cache()

file_names = ['2010-12-{place}-street.csv'.format(place=p) for p in ('west-yorkshire', 'wiltshire')]
data_directory = '/data/ukpolice/2010-12'
wy_df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('{}/{}'.format(data_directory, file_names[0]))
wi_df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('{}/{}'.format(data_directory, file_names[1]))
unified_df = wy_df.unionAll(wi_df)
print(unified_df.show())