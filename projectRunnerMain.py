from tkinter import *
import json
#Indentions were making me contemplate death, so I just rewrote the CLI.

#Just made it a public function because I'm lazy ? ?
def getS(time_str):
    m, s = time_str.split(':')
    return int(m) * 60 + int(s)



class start:
    def __init__(self):
        self.x = 0
    def buildMain():
        print('dab')
class gui:
    def __init__(self):
        print('')
    


class cli:

    def __init__(self):
        print('ok')
    def mainF(self):
        self.v = 1
        self.x = 1
        self.y = 5
        while(self.x != self.y):
            #Run through, append data, dump to json, start over, until x = 5
            self.runnerName = input("[Runner Name]: ")
            self.runnerTime = input("[Runner Time]: ")
            
            """Converting time to seconds
            if non numerical value, restarts
            function. We will add some GUI
            functions within this"""
            try:
                self.v = getS(self.runnerTime)
                print(self.v)
            except:
                print("Something went wrong.")
                cliS = cli()
                cliS.mainF()
            
            with open('runner.json', 'a') as self.runnerData:
                json.dump({self.x:[{'RunnerName' : self.runnerName, 'RunnerTime' : self.v}]}, self.runnerData)
                self.runnerData.close()
            self.x = self.x + 1
            cliS = cli()
            cliS.pData()
    def pData(self):
        self.runner = 1
        self.x = 1
        self.y = 5
        while(self.x!=self.y):
            with open('runner.json', 'r') as self.runnerDataFile:
                self.runnerData = json.load(self.runnerDataFile)
            self.runnerName = self.runnerData[self.runner]['RunnerName']
            self.runnerTime = self.runnerData[self.runner]['RunnerTime']
            print(self.runner)
            print(self.runnerName)
            print(self.runnerTime)
            self.runner = self.runner + 1
            self.x = self.x + 1
            



cliS = cli()
cliS.mainF()
