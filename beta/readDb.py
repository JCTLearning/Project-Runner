#ReadDataBase
import sqlite3 as lite

conn = lite.connect('vdotDb.db')
c = conn.cursor()

c.execute("select * from vdot")
x = c.fetchall()
for items in x:
    print(items)
