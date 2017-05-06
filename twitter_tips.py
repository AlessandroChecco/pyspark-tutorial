"""Example code for running pyspark on the twitter data set."""

from __future__ import print_function
import pyspark
from pyspark import SparkContext
from pyspark.sql import SQLContext, DataFrame
from pyspark.sql.functions import desc, mean

sc = SparkContext()
sqlContext = SQLContext(sc)

df = sqlContext.read.json('/data/INF6032Coursework/statuses.log.2014-12-30.gz')

# clean df and select the columns are are interested in
df = df.na.drop(subset=["user.id"]).select(["user","entities", "lang", "retweeted", "favorited"])

# view the contents of a column
print(df.select('lang').show())

# list the most common languages
print(df.groupby('lang').count().sort(desc('count')).show())

# get a dataframe of the user data
user_df = df.select('user.*')

# count of tweets per user
tweeters = user_df.groupby('screen_name').count()

# show how many times the most active users have tweeted
print(tweeters.sort(desc('count')).show())

# show the mean number of tweets per person
print(tweeters.select(mean('count')).show())

# get a dataframe of the users and the retweeted / favorited status
# This allows us to select values that are contained in nested dataframes
refined_df = df.select(['user.favourites_count', 'user.followers_count',
                        'user.friends_count', 'user.statuses_count', 'lang',
                        'retweeted', 'favorited'])
print(refined_df.describe().show())
