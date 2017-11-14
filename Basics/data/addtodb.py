import sqlite3 as lite
import json
class start:
	def __init__(self):
		self.x = 1
	def addToJson(self):

		self.runnerid = input('[Runner ID]: ')
		self.runnerN = input('[Runner First Name]: ')
		self.runnerL = input('[Runner Last Name]: ')
		self.runnerR1 = input('[Race Time 1]: ')
		self.runnerR2 = input('[Race Time 2]: ')
		self.runnerR3 = input('[Race Time 3]: ')
		self.runnerM = input('[Runner Mile Adv]: ')
		self.runnerPB = input('[Runner PB]: ')
		with open('testRunners/'+self.runnerN+'.json', 'w') as jsonFile:
			print('Are you sure you want to add...')
			print('id: '+self.runnerid+', fname: '+self.runnerN+', lname: '+self.runnerL+', r1: '+self.runnerR1+', r2: '+self.runnerR2+', r3: '+self.runnerR3+', mile: '+self.runnerM+', pb: '+self.runnerPB)
			self.a = input('[y/n]: ')
			if(self.a=='y'):
				json.dump({'id':self.runnerid,'fname':self.runnerN,'lname':self.runnerL,'r1':self.runnerR1,'r2':self.runnerR2, 'r3':self.runnerR3,'mile':self.runnerM,'pb':self.runnerPB}, jsonFile, indent = 4)
				pass
			else:
				pass
		print('Would you like to add this data to the data base?')
		self.a = input('[y/n]: ')
		if(self.a=='y'):
			conn = lite.connect('runner.db')
			c = conn.cursor()
			print('Attempting to create tables...')
			try:
				c.execute("CREATE TABLE Identification(runnerID TEXT, fname TEXT, lname TEXT)")c.execute("CREATE TABLE Identification(runnerID TEXT, fname TEXT, lname TEXT)")
				c.execute("CREATE TABLE Stats(r1 TEXT, r2 TEXT, r3 TEXT, mile TEXT, pb TEXT)")
				c.execute("CREATE TABLE Team(Avg TEXT)")
				print('Tables were made')
				
			except:
				print('Tables already exsist...')
				
			print('Adding data')
			c.execute("insert into Identification (runnerID, fname, lname) values (?, ?, ?)",(self.runnerid, self.runnerN, self.runnerL))
			c.execute("insert into Stats (r1, r2, r3, mile, pb) values (?, ? , ?, ?, ?)",(self.runnerR1,self.runnerR2,self.runnerR3,self.runnerM,self.runnerPB))
			print('Data added...')
			conn.commit()
			c.close()
			
			
s = start()
s.addToJson()
