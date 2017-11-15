import sqlite3 as lite
dataList = []
advNum = 0
totalnum = 1
class data:
	def __init__(self):
		self.x = 0
	def adv(self):
		
		self.advNum = 0
		self.totalNum = 0
		self.conn = lite.connect('runner.db')
		self.c = self.conn.cursor()
		self.c.execute("select * from Stats")
		self.data = self.c.fetchall()
		self.race = 0
		for self.items in self.data:
		
			for self.time in self.data:
				self.strTime = str(self.time[self.race])
				m, s = self.strTime.split(':')
				self.total = int(m)*60
				self.total = self.total+int(s)
				self.advNum = int(self.advNum) + int(self.total)
				self.totalNum = int(self.totalNum) + 1
			print(self.advNum)
			print(self.totalNum)
			self.raceAdv = int(self.advNum) / int(self.totalNum)
			print(self.raceAdv)
			self.mins = str(int(self.raceAdv) / 60)
			self.mins, self.undeeded = self.mins.split('.')
			self.mins = str(self.mins)
			self.seconds = int(int(self.mins) * 60)
			self.seconds = int(self.raceAdv - self.seconds)
			self.seconds = str(self.seconds)
			print('Race '+str(self.race+1)+': '+self.mins+':'+self.seconds)
			self.time = str(self.mins)+':'+str(self.seconds)
			dataList.insert(self.race, self.time)
			self.race = self.race + 1
		return dataList
dataC = data()
"""
Shows how we can get data, and take it out...
"""
x = dataC.adv()
for items in x:
	
	print(items)


"""
try:
	c.execute("CREATE TABLE Identification(runnerID TEXT, fname TEXT, lname TEXT)")
	c.execute("CREATE TABLE Stats(r1 TEXT, r2 TEXT, r3 TEXT, mile TEXT, pb TEXT)")
	c.execute("CREATE TABLE Team(Avg TEXT)")
	print('Tables were made')
except:
	print('Tables already exsisted...')
c.execute("create table teamStats(r1adv TEXT, r2adv TEXT, r3adv, mileadv TEXT)")
"""
