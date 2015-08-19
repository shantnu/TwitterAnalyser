import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
from local_config import *
import pdb
import json


class twitter_listener(StreamListener):

    def on_data(self, data):
        j = json.loads(data)
        print(j["text"])
        return True

    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(cons_tok, cons_sec)
    auth.set_access_token(app_tok, app_sec)
    twitter_api = tweepy.API(auth)

    twitter_stream = Stream(auth, twitter_listener())
    try:
        twitter_stream.sample()
    except Exception as e:
        print(e.__doc__)
