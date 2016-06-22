from twitter_api_auth import *
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from twitter_api_filterer import *


class StdOutListener(StreamListener):
    def on_data(self, data):
        with open('fetched_lupus_tweets.txt', 'a') as tf:
            text = json.loads(data)
            # filters tweets before storing them to see if they are related to lupus -WIP
            if api_filterer(text):
                # checks if the tweet has any valid geo data otherwise skips updating the json file
                if api_states(text):
                    # Updates geo data if there was a update to the geo data counter
                    save_new_geo_data()
                # Appends the new tweet to the list of previous tweets
                tf.write(data)
                # Prints the tweet into the console for visual observance of tweet coming in
                print('@%s : %s\n' % (text['user']['screen_name'], text['text']))
                return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # Loads the previous state tweet data into memory
    geo_data_init()

    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['lupus', '#lupusawarenessmonth', '#lupus', 'lupusawarenessmonth',
                         'lupus awareness month', '#TEAMLUPUS', '#beatlupus', 'lhandsign', '#lhandsign'])
