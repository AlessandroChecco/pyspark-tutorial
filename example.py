"""Find all months in a given year and count the crimes.

   This is useful when submitting a list of file names if
   a regex expression will not get you all the files you want.

   run as spark-submit example.py
"""

from __future__ import print_function
from functools import reduce
import pyspark
from pyspark import SparkContext
from pyspark.sql import SQLContext, DataFrame
sc = SparkContext("local", "pyspark")
sqlContext = SQLContext(sc)

def concat_all_dataframes(*args):
    """Concatenate all the dataframes given as input."""
    return reduce(DataFrame.unionAll, args)

place = 'west-yorkshire'
year = '2016'

# get a list of filenames that will be concatenated into a single frame
# the format has the 0 character before single numbers. 
# At the moment we don't have all months for 2016 in /data/ukpolice
months = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11')
file_names = ['/data/ukpolice/{year}-{month}/{year}-{month}-{place}-street.csv'.format(year=year,
                                                                                       month=m,
                                                                                       place=place) for m in months]

# load dataframes as a generator
annual_dataframes = (sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load(month)
                     for month in file_names)
annual_crimes = concat_all_dataframes(*annual_dataframes)
print(annual_crimes.groupby('Month').count().show())
