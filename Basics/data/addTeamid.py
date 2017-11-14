import sqlite3 as lite

conn = lite.connect('runner.db')
c = conn.cursor()
"""
#c.execute("CREATE TABLE teamData(teamid TEXT, mileadv TEXT)")
c.execute("insert into teamData(teamid, mileadv) values(?, ?)", ('1', '8:30'))
conn.commit()
c.close()
"""
c.execute("select * from teamData")
data = c.fetchone()
for elem in data:
	print(elem[0])
	break
