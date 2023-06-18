from fastapi import FastAPI
import psycopg2
# from contextlib import asynccontextmanager


# sql2 = '''COPY news(date, title, url, media)\
# FROM '/app/drought-tv-news.csv'\
# DELIMITER ','\
# CSV HEADER;'''
  
# cur.execute(sql2)
# conn.close()
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('before')
    yield
    print('after')


app = FastAPI(lifespan=lifespan)
gen = {}

# app = FastAPI()


@app.get("/init")
async def start():
    print('hhhh')
    conn = psycopg2.connect(
        host="postgres",
        user="fastapi",
        database="tvnews",
        password="azerty"
    )
    conn.autocommit = True
    cur = conn.cursor()

    sql = 'SELECT datname FROM pg_database;'
    cur.execute(sql)
    print(cur.fetchall())
    sql = "GRANT ALL ON database tvnews TO fastapi"
    cur.execute(sql)
    sql = '''CREATE TABLE IF NOT EXISTS news(\
    id SERIAL,\
    date varchar(50),\
    title varchar(250),\
    url text,\
    media varchar(200));'''
    cur.execute(sql)
    sql2 = '''COPY news(date, title, url, media)\
    FROM '/app/drought-tv-news.csv'\
    DELIMITER ','\
    CSV HEADER;'''
    cur.execute(sql2)

    sql = "SELECT * FROM news"
    cur.execute(sql)

    return [cur.fetchall()]



@app.get("/")
async def ping():
    return {"msg": "pong"}


@app.get("/postgres")
async def select():
    return {"msg": "bonjour"}
