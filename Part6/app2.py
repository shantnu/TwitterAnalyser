from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("lang.html")

@app.route("/top_tweets")
def top_tweets():
    return render_template("top_tweets.html")

@app.route("/trends")
def trends():
    return render_template("trends.html")

if __name__ == "__main__":
    app.run(debug = True)    