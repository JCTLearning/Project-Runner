import os
import json
from tkinter import *
import sqlite3 as lite
"""
-t = taylor note
"""

class gui:
	def __init__(self):
		"""
		Here is where we would start defining vars, or the db files we need to grab etc, etc.
		"""
	def mainPage(self):
		self.root = Tk()
		self.root.geometry("600x1000")

		"""
		Frames
		"""
		self.mainFrame = Frame(self.root)
		self.teamsFrame = Frame(self.mainFrame)
		self.runnersFrame = Frame(self.mainFrame)
		"""
		Pack Frames
		"""
		self.mainFrame.pack(anchor = "center")
		self.teamsFrame.grid(column = 0)
		self.runnersFrame.grid(column = 1)

		"""
		Basic Buttons To Change Pages
		"""
		self.teamButton = Button(self.teamsFrame, text="Teams", command = lambda: [self.mainFrame.pack_forget(), self.buildTeam()])
		self.teamButton.grid()

		self.runnersButton = Button(self.runnersFrame, text='Runners', command=lambda: [self.mainFrame.pack_forget(), self.buildRunners()])
		self.runnersButton.grid()


		self.root.mainloop()
	def buildTeam(self):
		print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Start of Team Page building...')

		"""
		Frames
		"""
		self.mainFrame = Frame(self.root)
		self.mainPageBut = Frame(self.mainFrame)
		self.teamDisplayFrame = Frame(self.mainFrame)
		self.runnersFrame = Frame(self.mainFrame)
		self.canvas = Canvas(self.mainFrame)
		self.teamStatsFrame = Frame(self.canvas)
		"""
		Pack Frames
		"""
		self.mainFrame.grid()
		self.mainPageBut.grid(column = 0, row = 0)
		self.teamDisplayFrame.grid(column = 1, row = 0)
		self.runnersFrame.grid(column = 1, row = 1)
		self.teamStatsFrame.grid(column = 1, row = 1)
		"""
		Scroll Wheel Hell
		"""
		self.scrollb = Scrollbar(self.root, orient="vertical",command=self.canvas.yview)
		self.canvas['yscrollcommand'] = self.scrollb.set   #attach scrollbar to frameTwo - t
		self.canvas.create_window((0,0),window=self.teamStatsFrame,anchor='nw')
		self.scrollb.grid(row=1, column=1, sticky='nsew')
		self.teamStatsFrame.bind("<Configure>", self.scrollFunction)
		self.scrollb.grid_forget()

		self.canvas.grid(row = 2, column = 0)



		"""
		Main Page Call Back
		"""
		self.mainPageButton = Button(self.mainPageBut, text = 'Main Page', command = lambda: [self.root.destroy(), self.mainPage()]) #self.mainFrame.pack_forget() Doesn't work while calling mainpage because we create a new tkinter window...
		self.mainPageButton.grid()
		"""
		Team display
		"""

		dataC = data()
		self.teamId = dataC.fetchTeamId()

		self.teamBanner = Label(self.teamDisplayFrame, text= 'Team ID: '+self.teamId)
		self.teamBanner.grid()
		"""
		## this is commented out because in truth we don't need it. ##
		Runers display

		self.rowNum = 0
		if(self.canDb=='True'):
			self.conn = lite.connect('data/runner.db')
			self.c = self.conn.cursor()
			self.c.execute("select * from Identification")
			self.data = self.c.fetchall()
			for elem in self.data:
				self.output = 'ID:'+ elem[0]+' FName: '+ elem[1]+' LName: '+elem[2]
				self.runnerId = elem[0]
				locals()['runners%runnerId' % self.runnerId] = Label(self.runnersFrame, text = self.output)
				locals()['runners%runnerId' % self.runnerId].grid(row = self.rowNum)
				self.rowNum = self.rowNum + 1
		if(self.canDb=='False'):
			self.failureT = Label(self.runnersFrame, text='Failure -- Could not find db, or we has a importation error')
			self.failureT.grid()
		"""
		dataC = data()
		self.canDb = dataC.openDataBase() #Goes ahead and checks for database
		"""
		Team stats
		"""
		"""
		PRINT RUNNER STATS
		"""
		if(self.canDb=='True'):
			self.total = dataC.getTotalNumberOfRunners()
			self.total = int(self.total)+1 #Allows us to use a != statement and still get the last result :p -t
			self.i = 1
			self.rowNum = 1
			while(self.i!=self.total):
				self.runnerStats = dataC.getDataOnTeam(self.i)

				"""
				Fix the output below where each item in the data list gets in own column :P
				"""
				print(self.output)
				locals()['runnerStat%runner' % self.i] = Label(self.teamStatsFrame, text = self.runnerStats)
				locals()['runnerStat%runner' % self.i].grid(row = self.rowNum)
				self.i = int(self.i) + 1
				self.rowNum = int(self.rowNum) + 1
		#ss

		self.x = 10
		while(self.x!=50):

			locals()['runnerStat%runner' % self.x] = Label(self.teamStatsFrame, text = self.x)
			locals()['runnerStat%runner' % self.x].grid(row = self.x)
			self.x = int(self.x) + 1

		#ss
		"""
		PRINT TEAM STATS
		"""
		if(self.canDb=='True'):
			self.teamRaceAdv = dataC.fetchTeamAdv()
			self.raceId = 1
			self.columnNum = 0
			for items in self.teamRaceAdv:
				locals()['race%raceId' % self.raceId] = Label(self.teamStatsFrame, text = 'Race'+str(self.raceId)+': '+str(items), borderwidth = 2)
				locals()['race%raceId' % self.raceId].grid(row = self.rowNum, column = self.columnNum )
				self.raceId = self.raceId + 1
				self.columnNum = self.columnNum + 1
		if(self.canDb=='False'):
			self.failureT2 = Label(self.runnersFrame, text='Failure -- Could not find db, or we has a importation error')
			self.failureT2.grid()
		self.scrollb.grid(sticky = 'ew')
		print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Build successfull...')
	def buildRunners(self):
		print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'start of runner GUI')

	def scrollFunction(self,event):
		"""
		This is apart of build scrolling
		"""
		#You need to set a max size for frameTwo. Otherwise, it will grow as needed --t
		self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=300,height=200)

class data:
	def __init__(self):
		self.x = False
		"""
		Here is where we should bring in our databases, and any other data bases.
		"""

	def openDataBase(self):
		print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Attempting to open up the data base...')
		try:

			self.conn = lite.connect('data/runner.db')
			self.c = self.conn.cursor()

			print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Data Base successfully opened...')
			self.c.close()
			return 'True'
		except:
			print('Could not connect to db file, make sure it exsists in the data folder, and runner.db is inside of that folder. Or just change the file pointer :shrug:')
			return 'False'
	def fetchTeamId(self):
		self.canDb = self.openDataBase()
		if(self.canDb=='True'):
			self.conn = lite.connect('data/runner.db')
			self.c = self.conn.cursor()
			self.c.execute("select * from teamData")
			self.data = self.c.fetchone()
			for elem in self.data:
				self.teamId = elem[0]
				break
			return self.teamId
	def fetchTeamAdv(self):
		"""
		The # prints are for math debug
		"""
		dataList = []
		self.advNum = 0
		self.totalNum = 0
		self.conn = lite.connect('data/runner.db')
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
			#print(self.advNum) -t
			#print(self.totalNum) -t
			self.raceAdv = int(self.advNum) / int(self.totalNum)
			#print(self.raceAdv) -t
			self.mins = str(int(self.raceAdv) / 60)
			self.mins, self.undeeded = self.mins.split('.')
			self.mins = str(self.mins)
			self.seconds = int(int(self.mins) * 60)
			self.seconds = int(self.raceAdv - self.seconds)
			self.seconds = str(self.seconds)
			#print('Race '+str(self.race+1)+': '+self.mins+':'+self.seconds) -t
			self.time = str(self.mins)+':'+str(self.seconds)
			dataList.insert(self.race, self.time)
			self.race = self.race + 1
		return dataList
	def getDataOnTeam(self, i):
		conn = lite.connect('data/runner.db')
		c = conn.cursor()
		c.execute("select * from Stats")
		data = c.fetchall()
		c.execute("select * from Identification")
		teamData = c.fetchall()
		self.dataRow = '1'
		i = str(i)
		for elem in data:
			if(self.dataRow!=i):
				self.dataRow = str(int(self.dataRow)+1) #Since we're not on the right row we're gonna add a row and repackage then try again  -t
				pass
			if(self.dataRow==i):
				self.dataRow = int(self.dataRow)+1 #we add this so it won't keep looping smh, logic could be fixed but eh it works - t
				self.dataRow = str(self.dataRow) #Repackage in a string - t
				for elem2 in teamData:


					if(elem2[0]!=i):
						pass
					if(elem2[0]==i):
						"""
						FORMAT OUTPUT AND RETURN IT
						"""
						#Can we get rid of the massive ammount of lines here or nah? (i mean i built it but idk)- t
						dbList = []
						elemNum = 0
						dbList.insert(elemNum, elem2[0])
						elemNum = elemNum + 1
						dbList.insert(elemNum, elem2[1])
						elemNum = elemNum + 1
						dbList.insert(elemNum, elem2[2])
						elemNum = elemNum + 1
						dbList.insert(elemNum, elem[0])
						elemNum = elemNum + 1
						dbList.insert(elemNum, elem[1])
						elemNum = elemNum + 1
						dbList.insert(elemNum, elem[2])

						return(dbList)
	def getTotalNumberOfRunners(self):
		conn = lite.connect('data/runner.db')
		c = conn.cursor()
		c.execute("select * from Identification")
		self.data = c.fetchall()
		self.numOfRunners = 0
		for items in self.data:
			self.numOfRunners = self.numOfRunners+1
		return(self.numOfRunners)
guiC = gui()
guiC.mainPage()
