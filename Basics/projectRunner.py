import os
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
		print('Start of Team Page building.')
		self.mainFrames = Frame(self.root)
		self.mainFrames.pack()
		self.title = Label(self.mainFrames, text='Teams')
		self.test.grid()
		#Define the main team page data stuff here
		
	def buildRunners(self):
		print('Building runner GUI')
		self.mainFrame = Frame(self.root)
		self.mainFrame.pack()
		self.title = Label(self.mainFrames, text='Runners')
		self.test.grid()
guiC = gui()
guiC.mainPage()




