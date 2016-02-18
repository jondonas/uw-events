from config import key
from config import mysql
from config import send_email
from config import send_bulk_email
import feedparser


feed = feedparser.parse('https://uwaterloo.ca/events/events/events.xml')

yourevents = []

for x in range(len(feed.entries)):
    yourevents.append((feed.entries[x].title, feed.entries[x].link))


conn = mysql.connect()
cursor = conn.cursor()

cursor.execute("SELECT * FROM users;")
subscribers = cursor.fetchall()

send_bulk_email(subscribers, yourevents, feed.feed.link)

cursor.close()
conn.close()
