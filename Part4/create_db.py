import sqlite3

db = "../twit_data.db"

conn = sqlite3.connect(db)
c = conn.cursor()

try:
    c.execute("drop table trend_data")
    c.execute("drop table twit_data")
    c.execute("drop table lang_data")
except:
    # Nothing to drop, do nothing.
    pass

cmd = "CREATE TABLE trend_data (trend TEXT, trend_id1 TEXT, trend_id2 TEXT, trend_id3 TEXT, datetime TEXT)"
c.execute(cmd)


cmd = "CREATE TABLE twit_data (top_tweet TEXT, datetime TEXT)"
c.execute(cmd)


cmd = "CREATE TABLE lang_data (language TEXT, top_language TEXT, datetime TEXT)"
c.execute(cmd)


conn.commit()

conn.close()