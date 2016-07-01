import json

GEO_DATA_FILENAME = 'geo_data_states.json'


def save_new_geo_data(state):
    # states_tweet_volume = {}
    with open(GEO_DATA_FILENAME, 'r') as infile:
        states_tweet_volume = json.load(infile)
    states_tweet_volume[state] += 1
    with open(GEO_DATA_FILENAME, 'w') as outfile:
        json.dump(states_tweet_volume, outfile)
    # file for html and javascript to read to know if geo_states_data was changed and then to reload tweetMap
    with open('geo_data_states_update_status.json', "w") as outfile:
        # File to save time stamp for comparison to see if geo_data_states.json has been updated since last call
        update_status = {"status": True}
        json.dump(update_status, outfile)
