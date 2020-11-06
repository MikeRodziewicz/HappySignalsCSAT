import psycopg2
import os

conn = psycopg2.connect(
    host="localhost",
    database="happy_signals",
    user= "postgres",
    password= os.getenv('DB_PASS'),
    port=5432
)

cur = conn.cursor()
cur.execute("""
DROP TABLE  test  """)
conn.commit()
cur.close()
conn.close()
