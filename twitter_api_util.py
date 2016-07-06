import json

GEO_DATA_FILENAME = 'geo_data_states.json'


# Saves new geo data for all tweets without a filter option for specific tweets
def save_new_geo_data(state):
    # states_tweet_volume = {}
    with open(GEO_DATA_FILENAME, 'r') as infile:
        states_tweet_volume = json.load(infile)
    states_tweet_volume[state] += 1

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

    # writes new geo data for passed option
    with open('Geo_data_optional_tweet_filters/%s_map_filter_options.json' % filter_option, 'w') as outfile:
        json.dump(states_tweet_volume, outfile)
