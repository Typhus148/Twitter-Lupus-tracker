import json
from twitter_api_states import list_states_full
from mapping import visualizeStateData

GEO_DATA_FILENAME = 'geo_data_states.json'


# Saves new geo data for all tweets without a filter option for specific tweets
def save_new_geo_data(state):
    # states_tweet_volume = {}
    with open(GEO_DATA_FILENAME, 'r') as infile:
        states_tweet_volume = json.load(infile)
    states_tweet_volume[state] += 1
    maximum_tweets(states_tweet_volume, 'tweetMap.json')

    # writes new geo data to file
    with open(GEO_DATA_FILENAME, 'w') as outfile:
        json.dump(states_tweet_volume, outfile)

    # file for html and javascript to read to know if geo_states_data was changed and then to reload tweetMap
    with open('geo_data_states_update_status.json', "w") as outfile:
        # File to save time stamp for comparison to see if geo_data_states.json has been updated since last call
        update_status = {"status": True}
        json.dump(update_status, outfile)


# Saves new geo data for tweets that are within the filter option
def save_new_geo_options_data(state, filter_option):
    # states_tweet_volume = {}
    with open('Geo_data_optional_tweet_filters/%s_map_filter_options.json' % filter_option, 'r') as infile:
        states_tweet_volume = json.load(infile)
    states_tweet_volume[state] += 1
    maximum_tweets(states_tweet_volume, ('Geo_data_optional_tweet_filters/%s_tweetMap.json' % filter_option))

    # writes new geo data for passed option
    with open('Geo_data_optional_tweet_filters/%s_map_filter_options.json' % filter_option, 'w') as outfile:
        json.dump(states_tweet_volume, outfile)


# Used to determine the thresh hold for the tweets to be bucketed in for graphing
def thresh_hold_calculator(max_Tweets):
    x = int(max_Tweets / 7)
    thresh_hold = [0] * 8
    i = 1
    z = 0
    y = 0
    while i <= 8:
        if i is 1:
            thresh_hold[z] = 0
            i += 1
            z += 1
        else:
            thresh_hold[z] = thresh_hold[y] + x
            i += 1
            z += 1
            y += 1
    return thresh_hold


# Gets the highest tweet counter in the state dictionary
def maximum_tweets(states_tweet_volume, file_name):
    max_Tweets = 0
    for state in list_states_full:
        if states_tweet_volume[state.title()] > max_Tweets:
            max_Tweets = states_tweet_volume[state.title()]
    visualizeStateData(states_tweet_volume, 'tweets', 'states', thresh_hold_calculator(max_Tweets), file_name)
