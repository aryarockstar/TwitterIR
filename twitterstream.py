import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

access_token = "75233164-gmXWvQP9KWf6vf7EZ6bpdeMYuOArCgBeVAiEEyR9J"
access_token_secret = "TGhj3kmvcR0YU4fIXr0L7ZvitubiSJea9EteqdVu4716g"
consumer_key = "hj5xvST7xW2bfU2azNKCNbTt6"
consumer_secret = "Fla5VkxUF3cz4f8vg4CZsq6WhaXFPI2QVwi9Iipo16HR8AsMRt"

# file name that you want to open is the second argument
save_file = open('data.json', 'a')

class listener(StreamListener):

    def on_data(self, data):
        #print data
        with open('test.txt','a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=['#FootballHighlights' ])
