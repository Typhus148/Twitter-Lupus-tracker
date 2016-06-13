import json
from twitter_api_auth import *
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


class StdOutListener(StreamListener):

    def on_data(self, data):
        # print data
        with open('fetched_lupus_tweets.txt', 'a') as tf:
            tf.write(data)
            decoded = json.loads(data)
            print('@%s: %s\n' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['lupus', '#lupusawarenessmonth', '#lupus', 'lupusawarenessmonth',
                         'lupus awareness month', '#TEAMLUPUS'])
