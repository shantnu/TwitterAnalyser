import tweepy
from local_config import *

a=tweepy.OAuthHandler(cons_tok, cons_sec)
a.set_access_token(app_tok, app_sec)
a2=tweepy.API(a)

# Search stuff
tt=tweepy.Cursor(a2.search, q = "Python").items(5)
for t in tt:
    print(t.text)

t2= a2.trends_place(1)

for t in t2[0]["trends"]:
    print(t['name'])
