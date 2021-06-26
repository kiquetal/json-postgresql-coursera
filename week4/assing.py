
# install psycopg2 (if needed)
# pip3 install psycopg2    # (or pip)

# https://www.pg4e.com/code/simple.py

# https://www.pg4e.com/code/hidden-dist.py
# copy hidden-dist.py to hidden.py
# edit hidden.py and put in your credentials

# python3 simple.py

# To check the results, use psql and look at the
# pythonfun table

import psycopg2
import hidden
import requests
import json

# Load the secrets
secrets = hidden.secrets()

conn = psycopg2.connect(host=secrets['host'],
        port=secrets['port'],
        database=secrets['database'],
        user=secrets['user'],
        password=secrets['pass'],
        connect_timeout=3)

cur = conn.cursor()

sql = 'DROP TABLE IF EXISTS pokeapi CASCADE;'
print(sql)
cur.execute(sql)

sql = 'CREATE TABLE pokeapi (id INTEGER, body JSONB);'
print(sql)
cur.execute(sql)

conn.commit()    # Flush it all to the DB server

for i in range(1,101):
    url = f"https://pokeapi.co/api/v2/pokemon/{i}"
    print(url)
    response = requests.get(url)
    text = response.text
    sql = 'INSERT INTO pokeapi(id,body) VALUES(%s,%s)'
    cur.execute(sql, (i, text))
conn.commit()

cur.close()

