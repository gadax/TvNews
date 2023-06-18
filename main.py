from fastapi import FastAPI
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="tvnews",
    password="azerty"
)

cur = conn.cursor()

sql = '''CREATE TABLE DETAILS(employee_id int NOT NULL,\
employee_name char(20),\
employee_email varchar(30), employee_salary float);'''
  
  
cursor.execute(sql)
  
sql2 = '''COPY details(employee_id,employee_name,\
employee_email,employee_salary)
FROM '/private/tmp/details.csv'
DELIMITER ','
CSV HEADER;'''
  

  
conn.close()



app = FastAPI()

@app.get("/")
async def ping():
    return {"msg": "pong"}


@app.get("/postgres")
async def select():
    cur.execute("SELECT")
    
    return {"msg": "bonjour"}
