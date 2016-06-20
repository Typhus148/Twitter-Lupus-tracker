from twitter_api_states import *


# Checks if lupus appears within the text of the tweet
def lupus_text_checker(text):
    word = 'lupus'
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    else:
        return False


# checks for whether some key words are in the tweet's text and if true flags the tweet as not related to lupus
# cleans the api data for irrelevant tweets
def tweet_filter(text):
    # word1 = 'homo'
    word2 = 'canis'
    word3 = 'homini'
    text = text.lower()
    # match1 = re.search(word1, text)
    match2 = re.search(word2, text)
    match3 = re.search(word3, text)

    if match3 or match2:
        return True
    else:
        return False


def api_filterer(text):
    if (lupus_text_checker(text['text']) == True) and (tweet_filter(text['text']) == False):
        api_states(text)
        return True
    else:
        return False
