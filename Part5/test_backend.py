import unittest
import sqlite3
from twit1 import *
import pdb
import ast
import warnings
warnings.simplefilter("ignore", ResourceWarning)

class TestTwit(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        c = self.conn.cursor()
        cmd = "CREATE TABLE trend_data (trend TEXT, trend_id1 TEXT, trend_id2 TEXT, trend_id3 TEXT, datetime TEXT)"
        c.execute(cmd)

        cmd = "CREATE TABLE twit_data (top_tweet TEXT, datetime TEXT)"
        c.execute(cmd)

        cmd = "CREATE TABLE lang_data (language TEXT, top_language TEXT, datetime TEXT)"
        c.execute(cmd)


        self.conn.commit()
        num_tweets_to_grab = 5
        retweet_count = 0
        self.twit = TwitterMain(num_tweets_to_grab, retweet_count, self.conn)

    def test_streaming_data(self):
        self.twit.get_streaming_data()
        try:
            lang, top_lang = self.read_data()
        except:
            self.fail("test_streaming_data: Nothing written to database. Test Failed.")

    def test_trends(self):
        self.twit.get_trends()      
        try:
            trend, trend_tweet = self.get_trends()
        except:
            self.fail("test_trends: Nothing written to database. Test Failed.")

    def test_stats(self):
        s = stats()
        s.add_lang("English")
        s.add_top_lang("Wooki")

        s.add_top_tweets("Tweet")


        lang, top_lang, top_tweets = s.get_stats()

        self.assertEqual(lang[0], "English")
        self.assertEqual(top_lang[0], "Wooki")
        self.assertEqual(top_tweets[0], "Tweet")



    def read_data(self):
        '''
        Shamelssly copied from app.py. Could be common, but I want to keep the tests independent of the code.
        '''
        
        self.conn.row_factory = sqlite3.Row
        c = self.conn.cursor()
        c.execute("SELECT * from lang_data ORDER BY datetime DESC LIMIT 1")

        result = c.fetchone()
        lang = ast.literal_eval(result['language'])
        top_lang = ast.literal_eval(result['top_language'])
      
        return lang, top_lang

    def get_trends(self):
        self.conn.row_factory = sqlite3.Row
        c = self.conn.cursor()

        trend = []
        trend_tweet = []

        c.execute("SELECT * from trend_data ORDER BY datetime DESC LIMIT 5") 
        result = c.fetchall()

        for r in result:
            trend.append(r['trend'])
            trend_tweet.append(r['trend_id1'])
            trend_tweet.append(r['trend_id2'])
            trend_tweet.append(r['trend_id3'])



        return trend, trend_tweet

    def tearDown(self):
        self.conn.close()

if __name__ == "__main__":
    unittest.main(warnings='ignore')