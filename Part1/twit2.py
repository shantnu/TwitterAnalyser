import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
from local_config import *
import pdb
import json

class l(StreamListener):

    def on_data(self, data):
            j = json.loads(data)
            print(j["text"])
            return True


    def on_error(self, status):
        print(status)

a=tweepy.OAuthHandler(cons_tok, cons_sec)
a.set_access_token(app_tok, app_sec)
a2=tweepy.API(a)


t1= Stream(a, l())    
t1.sample()
