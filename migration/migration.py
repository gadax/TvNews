import psycopg2
import os

if os.getenv("SCALINGO_POSTGRESQL_URL"):
	psycopg2.connect(os.getenv("SCALINGO_POSTGRESQL_URL"))
else:
	conn = psycopg2.connect(
		host="postgres",
		user="fastapi",
		database="tvnews",
		password="azerty"
	)

conn.autocommit = True
cur = conn.cursor()

def init():
	grant_right()
	create_schema()
	migrate()

	return cur


def grant_right():
	sql = "GRANT ALL ON database tvnews TO fastapi"
	cur.execute(sql)


def create_schema():
	sql = '''CREATE TABLE IF NOT EXISTS news(\
	id SERIAL,\
	date varchar(50),\
	title varchar(250),\
	url text,\
	media varchar(200));'''
	cur.execute(sql)


def migrate():
	sql = '''COPY news(date, title, url, media)\
	FROM '/app/drought-tv-news.csv'\
	DELIMITER ','\
	CSV HEADER;'''
	cur.execute(sql)