from mapping import visualizeStateData
from twitter_api_states import list_states_full


# Changes the value of the state given which has just been updated
def updated_state_color(states_tweet_volume, state):
    states_tweet_volume[state] = 999999 #TODO figure out what to store for said updated state
    maximum_tweets(states_tweet_volume, 'update_tweetMap.json')


# Used to determine the thresh hold for the tweets to be bucketed in for graphing
def thresh_hold_calculator(max_Tweets):
    x = int(max_Tweets / 7)
    thresh_hold = [0] * 9
    i = 1
    z = 0
    y = 0
    while i <= 7:
        if i is 1:
            thresh_hold[z] = 0
            i += 1
            z += 1
        else:
            thresh_hold[z] = thresh_hold[y] + x
            i += 1
            z += 1
            y += 1
    thresh_hold[8] = 999999 #TODO once input for updated state is known same goes here
    return thresh_hold


# Gets the highest tweet counter in the state dictionary
def maximum_tweets(states_tweet_volume, file_name):
    max_Tweets = 0
    for state in list_states_full:
        if states_tweet_volume[state.title()] is int:
            if states_tweet_volume[state.title()] > max_Tweets:
                max_Tweets = states_tweet_volume[state.title()]

    visualizeStateData(states_tweet_volume, 'tweets', 'states', thresh_hold_calculator(max_Tweets), file_name, True)
