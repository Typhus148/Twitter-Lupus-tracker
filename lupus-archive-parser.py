import json
import re

archive_Data = open('lupus-2015-archive.txt', 'r')
archive_File = open('lupus-2015-archive.txt', 'a')


def lupus_text_checker(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    else:
        return False


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
        if lupus_text_checker('lupus', tweets['text']):
            archive_File.write(tweets['created_at'])
            archive_File.write('@%s: %s\n' % (tweets['user']['screen_name'],
                                              tweets['text'].encode('ascii', 'ignore')))
            archive_File.write('\n')
            print(tweets['created_at'], '@%s: %s\n' % (tweets['user']['screen_name'],
                                                       tweets['text'].encode('ascii', 'ignore')))


archive_File.close()
archive_Data.close()

# archive_tweet = pd.DataFrame()
# archive_tweet['text'] = [x['text'] for x in tweets_Data]

# for line in archive_Data:
    # if 'lupus' in line:
        # print(line)
        # archive_File.write(line)
    # if 'lupus' in line:
        # print(line)
        # archive_File.write(line)

# for line in archive_Data:
    # for tweet in line.split('),('):
        # if 'lupus' in tweet:
            # print(tweet)
            # archive_File.write(tweet)
            # archive_File.write("),(")
        # if 'LUPUS' in tweet:
            # print(tweet)
            # archive_File.write(tweet)
            # archive_File.write("),(")

    # if count > 10:
        # break