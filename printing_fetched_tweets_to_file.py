#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "737646162820399104-MFFoB4Q0GkY6W9PCZRv51MzXWaHoOvN"
access_token_secret = "rR2Kd80DJbDYJFJlBJcjZLMrsn6Z7qemks40Zrz8In2EC"
consumer_key = "VFUVMZ3MLPNvWRnvLcJGV3qzc"
consumer_secret = "1ZFOZbL5lKtQBfI0ad2rjlQlnDIrwegHeWnSMzeFygkbogjJaC"

#myFile = open('fetched_lupus_tweets.txt', 'a');

class StdOutListener(StreamListener):

    def on_data(self, data):
        #print data
        with open('fetched_lupus_tweets.txt','a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['lupus', '#lupusawarenessmonth', '#lupus', 'lupusawarenessmonth'])