import psycopg2

conn = psycopg2.connect(host='127.0.0.1',
                        database='week',
                        user='myadmin',
                        password='paraguay',
                        connect_timeout=3)

cur = conn.cursor()
sql = 'DROP TABLE IF exists pythonfun CASCADE;'
cur.execute(sql)

sql = 'CREATE TABLE pythonfun (id SERIAL, line TEXT);'
print(sql)
cur.execute(sql)

conn.commit()

for i in range(10):
    txt = 'HAVE a nice day ' + str(i)
    sql = 'INSERT INTO pythonfun(line) VALUES (%s);'
    cur.execute(sql, (txt,))
conn.commit()

sql = 'SELECT id,line FROM pythonfun WHERE id=5'
print(sql)
cur.execute(sql)

row = cur.fetchone()
if row is None :
        print('Row not found')
else:
        print('FOund',row)

sql = 'INSERT INTO pythonfun (line) VALUES (%s)  RETURNING id;'
cur.execute(sql,(txt, ))
id = cur.fetchone()[0]
print('New id',id)

sql = 'SELECT line from pythonfun WHERE mistake=5;'
print(sql)
cur.execute(sql)

conn.commit()
cur.close()



print(cur)
