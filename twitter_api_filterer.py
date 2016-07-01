import re


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
    i = 0
    invalid_words = ['canis', 'homini', 'wolf', 'wolves']
    # word1 = 'homo'
    word = 'lhandsign'
    text = text.lower()
    match1 = re.search(word, text)
    while i < 4:
        match_list = re.search(invalid_words[i], text)
        if match_list:
            return True
        elif match1:
            return False
        else:
            i += 1
    return False


def lupus_api_filterer(text):
    if (lupus_text_checker(text['text']) == True) and (tweet_filter(text['text']) == False):
        return True
    else:
        return False
