
from pyspark.sql.functions import desc
# clean df
df = df.na.drop(subset=["user.id"]).select(["user","entities", "lang", "retweeted", "favorited"])

# list the most common languages
df.groupby('lang').count().sort(desc('count')).show()

# get a dataframe of the user data
user_df = df.select('user.*')

# get a datafrane of the hasttag data
df = df.select(["user.favourites_count", "user.followers_count","user.friends_count", "user.statuses_count", "lang", "retweeted", "favorited"])
