from fastapi import FastAPI
import psycopg2
import time
# from contextlib import asynccontextmanager


# sql2 = '''COPY news(date, title, url, media)\
# FROM '/app/drought-tv-news.csv'\
# DELIMITER ','\
# CSV HEADER;'''
  
# cur.execute(sql2)
# conn.close()

gen = {}

app = FastAPI()


@app.get("/init")
async def start():
    print('hhhh')
    conn = psycopg2.connect(
        host="postgres",
        user="fastapi",
        database="tvnews",
        password="azerty"
    )
    cur = conn.cursor()

    sql = 'SELECT datname FROM pg_database;'
    cur.execute(sql)
    print(cur.fetchall())
    sql = "GRANT ALL ON database tvnews TO fastapi"
    cur.execute(sql)
    conn.commit()
    sql = '''CREATE TABLE news(\
    id SERIAL,\
    date varchar(50),\
    title varchar(250),\
    url text,\
    media varchar(200));'''
    conn.commit()
    cur.execute(sql)
    sql2 = '''COPY news(date, title, url, media)\
    FROM '/app/drought-tv-news.csv'\
    DELIMITER ','\
    CSV HEADER;'''
      
    cur.execute(sql2)
    conn.commit()

    sql = "SELECT * FROM news"
    cur.execute(sql)
    print(cur.fetchall())



@app.get("/")
async def ping():
    return {"msg": "pong"}


@app.get("/postgres")
async def select():
    return {"msg": "bonjour"}
