def dropbox_main(data):
    # Use the file path to your dropbox app to save the file.
    file_to = u'/Users/typhus148/PycharmProjects/twitterapistreaming/Dropbox' \
              u'/Apps/twitter_lupus_bot/fetched_lupus_tweets.txt'
    with open(file_to, 'a') as f:
        f.write(data)
