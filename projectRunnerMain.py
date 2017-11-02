from tkinter import *

import json
class startUp:
	def __init__(self):
		self.x = 0
	def buildMain(self):
		print('Dk')


class cliCode:
	def __init__(self): #Define our vars here
		print('TEST')
	def mainFunct(self):

		self.x = 1
		self.y = 5 # shorting the var so we can lower run time
		while (self.x != self.y):
			self.runnerName = input("[Runner Name]: ")
			self.runnerTime = input("[Runner Time]: ")

			with open("runners.json", "w") as self.runnerData:
				json.dump({self.x: [{'RunnerName' : self.runnerName, 'RunnerTime': self.runnerTime}]}, self.runnerData)
				self.runnerData.close()
			self.x = self.x + 1# store it in the JSON here, top bracket as x, then data

		cliCodeC = cliCode()
		cliCodeC.printData()

# json.dump

	def printData(self):
		self.runner = 1
		self.x = 1 
		self.y = 5 # shorting the var so we can lower run time
		while(self.x!=self.y):
                        with open('runners.json', 'r') as self.runnerDataFile:
                                self.runnerData = json.load(self.runnerDataFile)
                        self.runnerName = self.runnerData[self.runner]['RunnerName']
                        self.runnerTime = self.runnerData[self.runner]['RunnerTime']
			print(self.runner)
			print(self.runnerName)
			print(self.runnerTime)
			self.runner = self.runner + 1 
			self.x = self.x + 1


cliCodeC = cliCode()
cliCodeC.mainFunct()
