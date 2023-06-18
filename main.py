from fastapi import FastAPI
import psycopg2

conn = psycopg2.connect(
    host="postgres",
    user="fastapi",
    database="tvnews",
    password="azerty"
)

cur = conn.cursor()

sql = '''CREATE TABLE news(\
id SERIAL,\
`date` varchar(50),\
title varchar(200),\
url varchar(200),\
media varchar(200));'''

sql2 = '''COPY persons(first_name, last_name, dob, email)\
FROM '/app/drought-tv-news.csv'\
DELIMITER ','\
CSV HEADER;'''
  
  
cur.execute(sql)
conn.close()


app = FastAPI()

@app.get("/")
async def ping():
    return {"msg": "pong"}


@app.get("/postgres")
async def select():
    
    return {"msg": "bonjour"}
