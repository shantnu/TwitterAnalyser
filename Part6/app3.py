from flask import Flask, render_template
import sqlite3
import ast

db = "../twit_data.db"

app = Flask(__name__)

def get_top_tweets():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("SELECT * from twit_data  ORDER BY datetime DESC LIMIT 30")
    result = c.fetchall()
    tweets = []

    datetime_toptweets = result[0]['datetime']

    for tweet in result:
        tweets.append(tweet['top_tweet'])
    
    conn.close()

    return tweets, datetime_toptweets

def get_trends():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    trend = []
    trend_tweet = []

    c.execute("SELECT * from trend_data ORDER BY datetime DESC LIMIT 10") 
    result = c.fetchall()

    datetime_trends = result[0]['datetime']

    for r in result:
        trend.append(r['trend'])
        trend_tweet.append(r['trend_id1'])
        trend_tweet.append(r['trend_id2'])
        trend_tweet.append(r['trend_id3'])

    conn.close()

    return trend, trend_tweet, datetime_trends

def get_lang():
    
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * from lang_data ORDER BY datetime DESC LIMIT 1")

    result = c.fetchone()
    lang = ast.literal_eval(result['language'])
    top_lang = ast.literal_eval(result['top_language'])
  
    conn.close()

    return lang, top_lang

@app.route("/")
def main():
    language_data = []
    top_language_data = []

    lang, top_lang = get_lang()
    for l in lang:
        language_data.append([l[0], l[1], l[1]])

    for t in top_lang:
        top_language_data.append([t[0], t[1], t[1]])
    return render_template("lang1.html", language_data = language_data, top_language_data = top_language_data)

@app.route("/top_tweets")
def top_tweets():
    tweets, datetime_toptweets = get_top_tweets()
    return render_template('top_tweets.html', tweets = tweets, datetime_toptweets = datetime_toptweets)

@app.route("/trends")
def trends():
    trend, trend_tweet, datetime_trends = get_trends()
    return render_template('trends.html', trend = trend, trend_tweet = trend_tweet, datetime_trends = datetime_trends)

if __name__ == "__main__":
    app.run(debug = True)    