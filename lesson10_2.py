import sqlite3
from lesson10_1 import init_db

db_name = 'mylibrary.db'
init_db(db_name)
conn = sqlite3.connect(db_name)
cur = conn.cursor()

cur.execute('SELECT * FROM author;')
print('Authors:')
rows = cur.fetchall()
print(rows)

cur.execute('SELECT * FROM book;')
print('Books:')
for row in cur:
    print(row)

cur.execute('INSERT INTO author(name) VALUES("Kirk HammetT")')
conn.commit()

cur.execute('SELECT * FROM author')
print("Authors 2:")
rows = cur.fetchall()
print(rows)

print("Select1:")
cur.execute('SELECT * FROM author WHERE id=%i' % 2)
print(cur.fetchone())

print('Select2:')
cur.execute('SELECT * FROM author WHERE id=?', (2,))
print(cur.fetchone())

cur.close()
conn.close()