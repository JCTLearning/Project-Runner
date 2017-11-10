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
		print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Build successfull...')
	def buildRunners(self):
		print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'start of runner GUI')



class data:
	def __init__(self):
		self.x = False
		"""
		Here is where we should bring in our databases, and any other data bases.
		"""
		"""
		Below is doing some weird formats so... I guess ill just define x here and leave init blank? I can never get init to work properly ://
		try:
			print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Fetching Data Base...')
			with open("data.json", "r") as self.dataFile:
				self.dbData = json.load(self.dataFile)
		except FileNotFoundError:
			print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'DB can not be found, creating one and populating it...')
			self.addDataToJson()
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
				pass
			except:
				print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Attempting to populate the JSON file...')
				self.addDataToJson()
			try:
				self.teamId = self.dbData['teamId']
				print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Successful fetching. Returning data now...')
				return self.teamId
			except:
				print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Json population attempt failed... exiting program.')
				import sys
				sys.exit()
	
guiC = gui()
guiC.mainPage()

