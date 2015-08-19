import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
from local_config import *
import pdb
import json


class twitter_listener(StreamListener):
    def __init__(self, num_tweets_to_grab):
        self.counter = 0
        self.num_tweets_to_grab = num_tweets_to_grab

    def on_data(self, data):
        try:
            j = json.loads(data)
            print(j["text"])
            self.counter += 1
            if self.counter == self.num_tweets_to_grab:
                return False

            return True
        except:
            # @TODO: Very dangerous, come back to this!
            pass

    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(cons_tok, cons_sec)
    auth.set_access_token(app_tok, app_sec)
    twitter_api = tweepy.API(auth)

    # Search stuff
    search_results = tweepy.Cursor(twitter_api.search, q="Python").items(5)
    for result in search_results:
        print(result.text)

    trends = twitter_api.trends_place(1)

    for trend in trends[0]["trends"]:
        print(trend['name'])
        
    twitter_stream = Stream(auth, twitter_listener(num_tweets_to_grab = 10))
    try:
        twitter_stream.sample()
    except Exception as e:
        print(e.__doc__)
