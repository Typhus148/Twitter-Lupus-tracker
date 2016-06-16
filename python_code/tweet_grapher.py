import json
import pandas
import vincent

tweets_File_Data = open('filtered_lupus_tweets.json', 'r')
tweets_Data = []
tweets_text = []

# tweets_File is the file pointer to the JSON data set

for line in tweets_File_Data:
    tweet = json.loads(line)
    # keys = tweet.keys()
    # print(keys)
    tweets_Data.append(tweet['created_at'])

# a list of "1" to count the #
ones = [1] * len(tweets_Data)
# the index of the series
idx = pandas.DatetimeIndex(tweets_Data)
# the actual series (at series of 1s for the moment)
lupus = pandas.Series(ones, index=idx)


# Resampling / bucketing
per_hour = lupus.resample('D').sum().fillna(0)

bar = vincent.Line(per_hour)
bar.axis_titles(x='Date', y='Amount of Tweets')
bar.to_json('time_chart.json')

tweets_File_Data.close()
