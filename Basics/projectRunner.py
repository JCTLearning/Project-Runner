import os
import json
from tkinter import *



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
		Gonna pull data from a json file for now...
		"""
		"""
		Frames
		"""
		self.mainFrame = Frame(self.root)
		self.mainPageBut = Frame(self.mainFrame)
		self.teamDisplayFrame = Frame(self.mainFrame)
		self.runnersFrame = Frame(self.mainFrame)
		self.teamStatsFrame = Frame(self.mainFrame)
		"""
		Pack Frames
		"""
		self.mainFrame.pack()
		self.mainPageBut.grid(column = 0, row = 0)
		self.teamDisplayFrame.grid(column = 1, row = 0)
		self.runnersFrame.grid(column = 1, row = 1)
		self.teamStatsFrame.grid(column = 0, row = 0)
		"""
		Main Page Call Back
		"""
		self.mainPageButton = Button(self.mainPageBut, text = 'Main Page', command = lambda: [self.root.destroy(), self.mainPage()]) #self.mainFrame.pack_forget() Doesn't work while calling mainpage because we create a new tkinter window... 
		self.mainPageButton.pack()
		"""
		Team display	
		"""
		dataC = data()
		self.teamId = dataC.getTeamId()
		self.teamBanner = Label(self.teamDisplayFrame, text= self.teamId)
		self.teamBanner.pack()
		"""
		Runers display
		"""
		self.rowNum = 0
		self.runnerId = 1
		self.runners = dataC.getRunners()

		for items in self.runners:
			self.runnerIdStr = str(self.runnerId)
			self.txt = 'Runner ID: '+self.runnerIdStr+' Name: '+items
			if(items!='null'):
				"""
				locals()['runners%runnerId' % self.runnerId] -- Creates a Var name based around the ID
				"""
				locals()['runners%runnerId' % self.runnerId] = Label(self.runnersFrame, text = self.txt)
				locals()['runners%runnerId' % self.runnerId].grid(row = self.rowNum)
				"""
				The debate is whether to create each runner graphic here, or not... it seenms logical todo so...
				"""
				
				self.runnerId = self.runnerId + 1
				self.rowNum = self.rowNum + 1
			else:
				pass
		
		print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Build successfull...')
	def buildRunners(self):
		print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'start of runner GUI')



class data:
	def __init__(self):
		self.x = False
		"""
		Here is where we should bring in our databases, and any other data bases.
		"""


	def openJson(self):
		print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Attempting to open the Db...')
		with open("data.json", "r") as self.dataFile:
			self.dbData = json.load(self.dataFile)
			
	def addDataToJson(self):
		print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Creating and populating a JSON file for use a temp data base...')
		with open("data.json", "w") as self.dataFile:
			json.dump({'teamId':'12', '1':'joe', '2':'rick', '3':'phfill'}, self.dataFile, indent = 4)
	def getTeamId(self):
		print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Fetching team id...')
		try:
			self.teamId = self.dbData['teamId']
			print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Successful fetching. Returning data now...')
			return self.teamId
		except:
			print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Either data fetch failed, or json file is not populated... Going to attempt to open json...')
			try:
				self.openJson()
				self.teamId = self.dbData['teamId']
				return self.teamId
				pass
			except:
				print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Attempting to populate the JSON file...')
				self.addDataToJson()
				self.teamId = self.dbData['teamId']
				return self.teamId				
	def getRunners(self):
		self.runnerList = []

		self.r1 = self.dbData['1']
		self.r2 = self.dbData['2']
		self.r3 = self.dbData['3']
		self.runnerList.insert(0, self.r1)
		self.runnerList.insert(1, self.r2)
		self.runnerList.insert(2, self.r3)
		self.runnerList.insert(3, 'null')
		return self.runnerList



guiC = gui()
guiC.mainPage()
