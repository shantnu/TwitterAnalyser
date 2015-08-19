import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
from local_config import *
import pdb
import json
from collections import Counter

langs = \
    {'ar': 'Arabic',
     'bg': 'Bulgarian',
     'ca': 'Catalan',
     'cs': 'Czech',
     'da': 'Danish',
     'de': 'German',
     'el': 'Greek',
     'en': 'English',
     'es': 'Spanish',
     'et': 'Estonian',
     'fa': 'Persian',
     'fi': 'Finnish',
     'fr': 'French',
     'hi': 'Hindi',
     'hr': 'Croatian',
     'hu': 'Hungarian',
     'id': 'Indonesian',
     'is': 'Icelandic',
     'it': 'Italian',
     'iw': 'Hebrew',
     'ja': 'Japanese',
     'ko': 'Korean',
     'lt': 'Lithuanian',
     'lv': 'Latvian',
     'ms': 'Malay',
     'nl': 'Dutch',
     'no': 'Norwegian',
     'pl': 'Polish',
     'pt': 'Portuguese',
     'ro': 'Romanian',
     'ru': 'Russian',
     'sk': 'Slovak',
     'sl': 'Slovenian',
     'sr': 'Serbian',
     'sv': 'Swedish',
     'th': 'Thai',
     'tl': 'Filipino',
     'tr': 'Turkish',
     'uk': 'Ukrainian',
     'ur': 'Urdu',
     'vi': 'Vietnamese',
     'zh_CN': 'Chinese (simplified)',
     'zh_TW': 'Chinese (traditional)'
     }


class twitter_listener(StreamListener):

    def __init__(self, num_tweets_to_grab):
        self.counter = 0
        self.num_tweets_to_grab = num_tweets_to_grab
        self.languages = []

    def on_data(self, data):
        try:
            json_data = json.loads(data)
            print(json_data["text"])
            self.languages.append(langs[json_data["lang"]])
            print(Counter(self.languages))

            self.counter += 1
            if self.counter == self.num_tweets_to_grab:
                print(self.languages)
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

    twitter_stream = Stream(auth, twitter_listener(num_tweets_to_grab=10))
    try:
        twitter_stream.sample()
    except Exception as e:
        print(e.__doc__)
