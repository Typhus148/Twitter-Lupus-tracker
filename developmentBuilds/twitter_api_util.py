import json

GEO_DATA_FILENAME = 'geo_data_states.json'

def save_new_geo_data(state):
    states_tweet_volume = {}
    with open(GEO_DATA_FILENAME, 'r') as infile:
       states_tweet_volume = json.load(infile)
    states_tweet_volume[state] += 1
    with open(GEO_DATA_FILENAME, 'w') as outfile:
        json.dump(states_tweet_volume, outfile)