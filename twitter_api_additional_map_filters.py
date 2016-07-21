import re
from twitter_api_util import save_new_geo_options_data

filter_options = ['lupus', 'lupusawarenessmonth', 'lupus awareness month', '#TEAMLUPUS', '#beatlupus', 'lhandsign']


# Checks accepted tweets to see if they contain one or more of the filter options text within the tweet
def specific_tweet_filter(tweet, filter_text):
    tweet = tweet.lower()
    filter_text = filter_text.lower()
    match = re.search(filter_text, tweet)
    if match:
        return True
    else:
        return False


# This function will be called to update every time a tweet is received and update all relevant geo tweet options
def update_geo_option_data(tweet_ld, state):
    x = 0
    while x < len(filter_options):
        if specific_tweet_filter(tweet_ld['text'], filter_options[x]):
            # add to state counter specific to option
            save_new_geo_options_data(state, filter_options[x])
        x += 1
