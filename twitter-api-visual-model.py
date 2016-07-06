from twitter_api_auth import consumer_key, consumer_secret, access_token, access_token_secret
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from twitter_api_filterer import lupus_api_filterer
from twitter_api_util import save_new_geo_data
import json
# from Dropbox_api_bot import Dropbox_api_app
from twitter_api_states import api_states
from twitter_api_additional_map_filters import update_geo_option_data


class StdOutListener(StreamListener):
    def on_data(self, data):
        with open('fetched_lupus_tweets.txt', 'a') as tf:
            text = json.loads(data)
            # filters tweets before storing them to see if they are related to lupus -WIP
            if lupus_api_filterer(text):
                # checks if the tweet has any valid geo data otherwise skips updating the json file
                state = api_states(text)
                if state is False:
                    update_status_file = open('geo_data_states_update_status.json', "r")
                    status_check = json.load(update_status_file)
                    update_status_file.close()
                    if status_check['status'] is True:
                        update_status_file = open('geo_data_states_update_status.json', "w")
                        update_status = {"status": False}
                        json.dump(update_status, update_status_file)
                        update_status_file.close()
                else:
                    # Updates geo data if there was a update to the geo data counter
                    save_new_geo_data(state)
                    update_geo_option_data(text, state)

                # Appends the new tweet to the list of previous tweets
                # Dropbox_api_app(data)
                tf.write(data)
                # Prints the tweet into the console for visual observance of tweet coming in
                print('@%s : %s\n' % (text['user']['screen_name'], text['text']))
                return True

    def on_error(self, status):
        print(status)


def lupus_tweet_tracker_setup():
    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['lupus', '#lupusawarenessmonth', '#lupus', 'lupusawarenessmonth',
                         'lupus awareness month', '#TEAMLUPUS', '#beatlupus', 'lhandsign', '#lhandsign'])


if __name__ == '__main__':
    lupus_tweet_tracker_setup()
