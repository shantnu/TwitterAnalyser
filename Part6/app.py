from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return "Most used languages on Twitter: All Tweets"

@app.route("/top_tweets")
def top_tweets():
    return "Most Popular Tweets"    

@app.route("/trends")
def trends():
    return "Trending On Twitter:"

if __name__ == "__main__":
    app.run(debug = True)    
