import sqlite3 as lite


class start:
	def __init__(self):
		self.x = 0
	def readWholeDb(self):
		conn = lite.connect('runner.db')
		c = conn.cursor()
		c.execute("select * from Identification")
		data = c.fetchall()
		for elem in data:
			print('ID:'+ elem[0]+' FName: '+ elem[1]+' LName: '+elem[2])
			#AFTER TWO HOURS OF COMPLETE BULL I FIGURED IT OUT REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
s = start()
s.readWholeDb()
