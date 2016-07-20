from twitter_api_auth import consumer_key, consumer_secret, access_token, access_token_secret
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from twitter_api_filterer import lupus_api_filterer
from twitter_api_util import save_new_geo_data, GEO_STATES_UPDATE_STATUS
import json
from twitter_api_states import api_states
from twitter_api_additional_map_filters import update_geo_option_data
from Dropbox_api_bot import dropbox_main


class StdOutListener(StreamListener):
    def on_data(self, data):
        with open('fetched_lupus_tweets.txt', 'a') as tf:
            text = json.loads(data)
            # filters tweets before storing them to see if they are related to lupus -WIP
            if lupus_api_filterer(text):
                # checks if the tweet has any valid geo data otherwise skips updating the json file
                state = api_states(text)
                if state is False:
                    with open(GEO_STATES_UPDATE_STATUS, 'r') as update_status_infile:
                        status_check = json.load(update_status_infile)
                    if status_check['status']:
                        update_status = {"status": False}
                        with open(GEO_STATES_UPDATE_STATUS, 'w') as update_status_outfile:
                            json.dump(update_status, update_status_outfile)
                else:
                    # Updates geo data if there was a update to the geo data counter
                    save_new_geo_data(state)
                    update_geo_option_data(text, state)

                # Appends the new tweet to the list of previous tweets
                dropbox_main(data)
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
                         'lupus awareness month', '#TEAMLUPUS', '#beatlupus', 'lhandsign', '#lhandsign',
                         '#lupusawareness', 'lupusawareness', 'lupus awareness'])


if __name__ == '__main__':
    print('Starting up lupus twitter bot...')
    lupus_tweet_tracker_setup()
