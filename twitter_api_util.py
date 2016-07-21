import json
from twitter_api_states import list_states_full
from mapping import visualizeStateData
from twitter_api_geo_update_color_map import updated_state_color

GEO_DATA_FILENAME = 'geo_data_states.json'
GEO_STATES_UPDATE_STATUS = 'geo_data_states_update_status.json'
GEO_OPTIONAL_FILTER_TWEETS_DIRECTORY = 'Geo_data_optional_tweet_filters/'
GEO_UPDATE_TWEETMAP = '_tweetMap.json'
GEO_DATA_OPTIONAL_FILTER = '_map_filter_options.json'


# Saves new geo data for all tweets without a filter option for specific tweets
def save_new_geo_data(state):
    # states_tweet_volume = {}
    with open(GEO_DATA_FILENAME, 'r') as infile:
        states_tweet_volume = json.load(infile)
    states_tweet_volume[state] += 1

    # writes new geo data to file
    with open(GEO_DATA_FILENAME, 'w') as outfile:
        json.dump(states_tweet_volume, outfile)
    maximum_tweets(states_tweet_volume, 'tweetMap.json')

    # file for html and javascript to read to know if geo_states_data was changed and then to reload tweetMap
    with open(GEO_STATES_UPDATE_STATUS, 'w') as outfile:
        # File to save time stamp for comparison to see if geo_data_states.json has been updated since last call
        update_status = {"status": True}
        json.dump(update_status, outfile)
    updated_state_color(states_tweet_volume, state)


# Saves new geo data for tweets that are within the filter option
def save_new_geo_options_data(state, filter_option):
    filter_option = filter_option.lower()

    if ' ' in filter_option:
        filter_option.replace(' ', '')

    # states_tweet_volume = {}
    # This is the json file that stores the counters for each state
    with open(GEO_OPTIONAL_FILTER_TWEETS_DIRECTORY + filter_option + GEO_DATA_OPTIONAL_FILTER, 'r') as infile:
        states_tweet_volume = json.load(infile)
    states_tweet_volume[state] += 1

    # writes new geo data for passed option
    with open(GEO_OPTIONAL_FILTER_TWEETS_DIRECTORY + filter_option + GEO_DATA_OPTIONAL_FILTER, 'w') as outfile:
        json.dump(states_tweet_volume, outfile)
    maximum_tweets(states_tweet_volume, (GEO_OPTIONAL_FILTER_TWEETS_DIRECTORY + filter_option +
                                         GEO_DATA_OPTIONAL_FILTER))
    updated_state_color(states_tweet_volume, state)


# Used to determine the thresh hold for the tweets to be bucketed in for graphing
def thresh_hold_calculator(max_Tweets):
    thresh_hold = [int(i * max_Tweets / 8) for i in range(0, 8)]
    return thresh_hold


# Gets the highest tweet counter in the state dictionary
def maximum_tweets(states_tweet_volume, file_name):
    max_Tweets = 0
    for state in list_states_full:
        if states_tweet_volume[state.title()] > max_Tweets:
            max_Tweets = states_tweet_volume[state.title()]
    visualizeStateData(states_tweet_volume, 'tweets', 'states', thresh_hold_calculator(max_Tweets), file_name, False)
