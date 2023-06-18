from fastapi import FastAPI
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="tvnews",
    password="azerty"
)

cur = conn.cursor()

app = FastAPI()

@app.get("/")
async def ping():
    return {"msg": "pong"}


@app.get("/postgres")
async def select():
    cur.execute("SELECT")
    
    return {"msg": "bonjour"}
