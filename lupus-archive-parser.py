import json
import re

archive_Data = open('fetched_lupus_tweets.txt', 'r')
archive_File = open('filtered_lupus_tweets.json', 'a')


# Checks if lupus appears within the text of the tweet
def lupus_text_checker(word, text):
    word = word.lower()
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


tweet_Counter = 0
good_Tweets = 0
invalid_Tweets = 0


for line in archive_Data:
    # prints amount of characters in line
    # print('Retrieved', len(line), 'characters')
    # possible_json_string = str(line)
    # print('possible_json_string')
    # prints current json parser is on
    # print(possible_json_string)
    tweets = json.loads(line)
    # checks if key is in tweets dictionary otherwise it skips
    if 'created_at' in tweets:
        tweet_Counter += 1
        # print('Current tweet being parsed:', tweet_Counter)
        if lupus_text_checker('lupus', tweets['text']):
            if tweet_filter(tweets['text']):
                invalid_Tweets += 1
                print('Tweet #', tweet_Counter, 'does not pertain to lupus and will not be used.')
            else:
                good_Tweets += 1
                archive_File.write(line)
                # archive_File.write(tweets['created_at'])
                # archive_File.write('@%s: %s\n' % (tweets['user']['screen_name'],
                #                                  tweets['text'].encode('ascii', 'ignore')))
                # print the tweets that will be written to file
                # print(tweets['created_at'], '@%s: %s\n' % (tweets['user']['screen_name'],
                #                                            tweets['text'].encode('ascii', 'ignore')))
        else:
            invalid_Tweets += 1
            print('Tweet #', tweet_Counter, 'does not contain lupus within the tweet and will not be used.')


print('Total tweets:', tweet_Counter, 'of which', good_Tweets, 'were verified as pertaining to lupus and ',
      invalid_Tweets, 'were discarded as they did not pertain to lupus.')
print(tweet_Counter, 'should be equal to', good_Tweets, '+', invalid_Tweets, '=', good_Tweets + invalid_Tweets)
archive_File.close()
archive_Data.close()
