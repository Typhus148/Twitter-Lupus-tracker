from mapping import visualizeStateData
import re
import json

# dictionary with counter values per state
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
# list of states
list_states_full = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware',
                    'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky',
                    'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi',
                    'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico',
                    'new york', 'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania',
                    'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas', 'utah', 'vermont',
                    'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming']
# abbreviation with no operation expressions
list_states_plain = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS',
                     'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY',
                     'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV',
                     'WI', 'WY']
# abbreviation with operation expressions
list_states = ['\bAL\b', '\bAK\b', '\bAZ\b', '\bAR\b', '\bCA\b', '\bCO\b', '\bCT\b', '\bDE\b', '\bFL\b', '\bGA\b',
               '\bHI\b', '\bID\b', '\bIL\b', '\bIN\b', '\bIA\b', '\bKS\b', '\bKY\b', '\bLA\b', '\bME\b', '\bMD\b',
               '\bMA\b', '\bMI\b', '\bMN\b', '\bMS\b', '\bMO\b', '\bMT\b', '\bNE\b', '\bNV\b', '\bNH\b', '\bNJ\b',
               '\bNM\b', '\bNY\b', '\bNC\b', '\bND\b', '\bOH\b', '\bOK\b', '\bOR\b', '\bPA\b', '\bRI\b', '\bSC\b',
               '\bSD\b', '\bTN\b', '\bTX\b', '\bUT\b', '\bVT\b', '\bVA\b', '\bWA\b', '\bWV\b', '\bWI\b', '\bWY\b']


# Checks whether location or coordinate field is null or not
def null_checker(text):
    if text is None:
        return True
    else:
        return False


# Changed return True to return the state that was tagged
# checks for state abbreviation in location key
def location_abbreviation_check(text):
    i = 0
    if len(text) == 2:
        for state in list_states_plain:
            match = re.search(state, text)
            if match:
                state_key = list_states_full[i]
                states_tweet_volume[state_key.title()] += 1
                return state_key.title()
            else:
                i += 1
    else:
        for state in list_states:
            match = re.search(state, text)
            if match:
                state_key = list_states_full[i]
                states_tweet_volume[state_key.title()] += 1
                return state_key.title()
            else:
                i += 1
    return False


# Changed return True to return the state that was tagged
# checks for state in location key if not abbreviated
def location_verify(text):
    text = text.lower()
    i = 0
    w1 = 'washington dc'
    w2 = 'washington, dc'
    w3 = 'washington d.c.'
    w4 = 'washington, pa'
    w5 = 'washington pa'
    match1 = re.search(w1, text)
    match2 = re.search(w2, text)
    match3 = re.search(w3, text)
    match4 = re.search(w4, text)
    match5 = re.search(w5, text)
    if match1:
        # states_tweet_volume['Virginia'] += 1
        return 'Virginia'
    if match2:
        # states_tweet_volume['Virginia'] += 1
        return 'Virginia'
    if match3:
        # states_tweet_volume['Virginia'] += 1
        return 'Virginia'
    if match4:
        # states_tweet_volume['Pennsylvania'] += 1
        return 'Pennsylvania'
    if match5:
        # states_tweet_volume['Pennsylvania'] += 1
        return 'Pennsylvania'
    for state in list_states_full:
        match = re.search(state, text)
        if match:
            # states_tweet_volume[state.title()] += 1
            return state.title()
        else:
            i += 1
    return False

# Outdated function will remove
# Loads saved geo data into the system to be used without starting from scratch
def geo_data_init():
    geo_data = open('geo_data_states.json', 'r')
    state_counter = json.load(geo_data)
    i = 0
    while i < 50:
        states_tweet_volume[list_states_full[i].title()] += state_counter[list_states_full[i].title()]
        i += 1

    geo_data.close()


# Outdated function will remove
# Updates the geo data json with any new additions of tweets to a state counter
def save_new_geo_data():
    geo_data = open('geo_data_states.json', "w")
    json.dump(states_tweet_volume, geo_data)
    geo_data.close()
    update_status_file = open('geo_data_states_update_status.json', "w")
    # File to save time stamp for comparison to see if geo_data_states.json has been updated since last call
    update_status = {"status": True}
    json.dump(update_status, update_status_file)
    update_status_file.close()


# Used to determine the thresh hold for the tweets to be bucketed in for graphing
def thresh_hold_calculator(maxTweets):
    x = int(maxTweets / 7)
    threshhold = [0] * 8
    i = 1
    z = 0
    y = 0
    while i <= 8:
        if i is 1:
            threshhold[z] = 0
            i += 1
            z += 1
        else:
            threshhold[z] = threshhold[y] + x
            i += 1
            z += 1
            y += 1
    return threshhold


# Gets the highest tweet counter in the state dictionary
def maximum_tweets():
    maxTweets = 0
    for state in list_states_full:
        if states_tweet_volume[state.title()] > maxTweets:
            maxTweets = states_tweet_volume[state.title()]
    visualizeStateData(states_tweet_volume, 'tweets', 'states', thresh_hold_calculator(maxTweets))


# Function to be called to check a tweet for location information and add it to the map/graph
def api_states(tweet_LG):
    state_result1 = location_abbreviation_check(tweet_LG['user']['location'])
    state_result2 = location_abbreviation_check(tweet_LG['user']['location'])
    if null_checker(tweet_LG['user']['location']) is False:
        # if no valid state from searching for full state names check for abbreviations
        if state_result1 is False:
            # if abbreviation returns false then it will return the state abbreviated in tweet
            if state_result2 is False:
                return False
            maximum_tweets()
            return state_result2
        maximum_tweets()
        return state_result1
    return False
