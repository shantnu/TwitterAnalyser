from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import sqlite3
from twit1 import *
import requests

class TestFlask(unittest.TestCase):

    def test_web_app_running(self):
        try:
             r =requests.get("http://127.0.0.1:5000/")
        except:
            self.fail("Could not open web app. Not running, or crashed. Test Failed")


    def test_lang(self):

        r = requests.get("http://127.0.0.1:5000/")
        page_src = r.text

        if page_src.find("Most used languages on Twitter: All Tweets") < 0:
            self.fail("Can't find most common languages")


    def test_top_tweets(self):
        r = requests.get("http://127.0.0.1:5000/top_tweets")
        page_src = r.text

        if page_src.find('Most Popular Tweets') < 0:
            self.fail("Top tweets failed")

        if page_src.find('<blockquote class="twitter-tweet') < 0:
            self.fail("Can't find the top tweets")

    def test_trends(self):
        r = requests.get("http://127.0.0.1:5000/trends")
        page_src = r.text

        if page_src.find('Trending On Twitter:') < 0:
            self.fail("Trends failed")

        if page_src.find('<blockquote class="twitter-tweet') < 0:
            self.fail("Can't find the trending tweets")

if __name__ == "__main__":
    unittest.main(warnings='ignore', failfast = True)