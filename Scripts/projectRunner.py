import os
import json
from tkinter import *
import sqlite3 as lite


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
		self.teamId = dataC.fetchTeamId()

		self.teamBanner = Label(self.teamDisplayFrame, text= 'Team ID: '+self.teamId)
		self.teamBanner.pack()
		"""
		Runers display
		"""
		self.rowNum = 0
		dataC = data()
		self.canDb = dataC.openDataBase()
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
		for items in self.runners:
			self.runnerIdStr = str(self.runnerId)
			self.txt = 'Runner ID: '+self.runnerIdStr+' Name: '+items
			if(items!='null'):
				
				#locals()['runners%runnerId' % self.runnerId] -- Creates a Var name based around the ID
				
				locals()['runners%runnerId' % self.runnerId] = Label(self.runnersFrame, text = self.txt)
				locals()['runners%runnerId' % self.runnerId].grid(row = self.rowNum)

				
				self.runnerId = self.runnerId + 1
				self.rowNum = self.rowNum + 1
			else:
				pass
		"""
		print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Build successfull...')
	def buildRunners(self):
		print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'start of runner GUI')



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
guiC = gui()
guiC.mainPage()
