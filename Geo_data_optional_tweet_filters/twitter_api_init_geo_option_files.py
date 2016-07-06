import json
from twitter_api_states import api_states
from twitter_api_util import save_new_geo_options_data
from twitter_api_additional_map_filters import specific_tweet_filter


'''def init_filter_option_files(filter_option):
    states_tweet_volume = {"Alabama": 0, "Alaska": 0, "Arizona": 0, "Arkansas": 0, "California": 0,
                           "Colorado": 0, "Connecticut": 0, "Delaware": 0, "Florida": 0, "Georgia": 0,
                           "Hawaii": 0, "Idaho": 0, "Illinois": 0, "Indiana": 0, "Iowa": 0, "Kansas": 0,
                           "Kentucky": 0, "Louisiana": 0, "Maine": 0, "Maryland": 0, "Massachusetts": 0,
                           "Michigan": 0, "Minnesota": 0, "Mississippi": 0, "Missouri": 0, "Montana": 0,
                           "Nebraska": 0, "Nevada": 0, "New Hampshire": 0, "New Jersey": 0, "New Mexico": 0,
                           "New York": 0, "North Carolina": 0, "North Dakota": 0, "Ohio": 0, "Oklahoma": 0,
                           "Oregon": 0, "Pennsylvania": 0, "Rhode Island": 0, "South Carolina": 0,
                           "South Dakota": 0, "Tennessee": 0, "Texas": 0, "Utah": 0, "Vermont": 0,
                           "Virginia": 0, "Washington": 0, "West Virginia": 0, "Wisconsin": 0, "Wyoming": 0}
    with open('%s_map_filter_options.json' % filter_option, 'w') as outfile:
        json.dump(states_tweet_volume, outfile)'''


# This function is only used to create the initial base options from already collected tweets
def create_base_options(filter_key_words):
    fetched_tweets = open('fetched_lupus_tweets.txt', 'r')

    for line in fetched_tweets:
        tweet = json.loads(line)
        i = 0
        while i < len(filter_options):
            if specific_tweet_filter(tweet['text'], filter_key_words[i]):
                state_of_tweet = api_states(tweet)
                if state_of_tweet:
                    save_new_geo_options_data(state_of_tweet, filter_key_words[i])
                i += 1
            else:
                i += 1
    fetched_tweets.close()


if __name__ == '__main__':
    filter_options = ['lupus', '#lupusawarenessmonth', '#lupus', 'lupusawarenessmonth',
                      'lupus awareness month', '#TEAMLUPUS', '#beatlupus', 'lhandsign', '#lhandsign']
    '''x = 0
    while x < len(filter_options):
        init_filter_option_files(filter_options[x])
        x += 1'''
    # reads all currently saved tweets and saves them to their corresponding json file
    create_base_options(filter_options)
