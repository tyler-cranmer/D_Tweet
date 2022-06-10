import tweepy
import config
import json
from time import sleep


class Tweepy:
    def __init__(self, _bearer_token, _consumer_key, _consumer_secret, _access_token, _access_token_secret):
        self.client  = tweepy.Client(bearer_token= _bearer_token,
                        consumer_key=_consumer_key, 
                        consumer_secret=_consumer_secret, 
                        access_token=_access_token, 
                        access_token_secret=_access_token_secret,)

    def getUserId(self, username):
        client = self.client
        user = client.get_user(username=username).data.id
        return user

class MyStream(tweepy.StreamingClient):

    def on_connect(self):
        print("Connected")

    def on_tweet(self, tweet):
        # if tweet.referenced_tweets == None: //this will filter out retweet. need to call with params -> stream.filter(tweet_fields=["referenced_tweets"])
        print(tweet.id)
        print(tweet.text)
        return tweet.id



if __name__ == '__main__':

    bearer_token=config.BEARER_TOKEN
    stream = MyStream(bearer_token=bearer_token)
    # stream.add_rules(tweepy.StreamRule('from:0xNeferfeeti'))
    print(stream.get_rules())
    stream.filter()
