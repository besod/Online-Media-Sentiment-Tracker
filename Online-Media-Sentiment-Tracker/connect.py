import sqlite3
import datetime 

class Connect:   
    '''This class will connect to SQLite databse file 'media.db'. A table named articles
    store the topic,title and url of scraped data.''' 
    def __init__(self,title,topic,url):
        self.topic = topic
        self.title = title
        self.url = url
           
    def save_to_db(self):
        currentdate = datetime.datetime.now().date()
        conn = sqlite3.connect("newsArticle.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS articles  (
            date DATE,
            topic TEXT NOT NULL,
            title TEXT NOT NULL,
            url TEXT NOT NULL
            )""")
        conn.commit()
           
        c.execute("""SELECT title FROM articles""")
        result=c.fetchone
        
        #if result is None:
        c.execute("""INSERT INTO articles VALUES (?, ?, ?, ?)""",
                  (currentdate, self.title, self.url, self.topic))
        conn.commit()
        print("Article saved successfully!\n")
            
        conn.close()