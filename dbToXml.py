import sqlite3 as lite
import xml.etree.cElementTree as Et

"""
DB
"""
class startUp:
    def __init__(self):
        self.y = 1
    def main(self):
        root = Et.Element('root')
        run = Et.SubElement(root, "Runners")
        conn = lite.connect("Data/TeamOne.db")
        c = conn.cursor()
        c.execute("select * from Identification")
        teamData = c.fetchall()
        dataC = data1()
        loopNum = int(dataC.getTotalRunners())
        loopNum = loopNum + 2 #Idk why I have todo this tbh... but it works
        currentNum = 2 #Current row Because if you start on 1, you get two john rancers...
        print('starting')
        while(currentNum != loopNum):
            list1 = dataC.getData(currentNum)
            print(currentNum)
            runnerIdent = dataC.getIndvData(currentNum)
            runnerid = runnerIdent[0]
            runnerName = str(runnerIdent[1])+' '+str(runnerIdent[2])
            Runner = Et.SubElement(run, "ID", id = runnerid )
            print(str(list1)+'ssss')
            Et.SubElement(Runner, "Name", name = runnerName)
            Et.SubElement(Runner, "Races", race1 = list1[0], race2 = list1[1], race3 = list1[2])
            currentNum = currentNum + 1

            """
            XML
            """
        print('done')
        tree = Et.ElementTree(root)
        tree.write("runner1.xml")
class data1:
    def __init__(self):
        #Its easier to build the data here...
        x = 2
    def getData(self, RunNum):
        dataC = data1()
        self.canDb = 'True'
        if(self.canDb=='True'):
            self.total = dataC.getTotalRunners()
            self.total = int(self.total)+1 #Allows us to use a != statement and still get the last result :p -t
            self.i = RunNum
            self.rowNum = 1
            #while(self.i!=self.total):
            self.runnerStats = dataC.getRaces(self.i)

            """
            Fix the output below where each item in the data list gets in own column :P
            """
            print('NewLine')
            dbList = []
            self.listNum = 0
            for items in self.runnerStats:
                dbList.insert(self.listNum, items)
                print(dbList)
                self.listNum = self.listNum + 1
            return(dbList)
    def getTotalRunners(self):
        conn = lite.connect('Data/TeamOne.db')

        c = conn.cursor()
        c.execute("select * from Identification")
        data = c.fetchall()
        numOfRunners = 0
        for items in data:
            numOfRunners = numOfRunners+1
        return(numOfRunners)
    def getRaces(self, rid):
        conn = lite.connect('Data/TeamOne.db')

        c = conn.cursor()
        c.execute("select * from Stats")
        data = c.fetchall()
        self.x = 1 #row for db
        raceDb = []
        for items in data:
            if(rid!=self.x):
                self.x = self.x + 1
                print('w:'+str(items))
                pass
            if(rid==self.x):
                raceDb = items
                print('r'+str(raceDb))
                return raceDb
    def getIndvData(self, rid):
        conn = lite.connect('Data/TeamOne.db')
        c = conn.cursor()
        c.execute("select * from Identification")
        dataList = c.fetchall()
        self.x = 1
        for list1 in dataList:
            if(self.x!=rid):
                self.x = self.x + 1
                pass
            if(self.x==rid):
                db = []
                db = list1
                print(db)
                return db

startupC = startUp()
startupC.main()
