from tkinter import *

import sqlite3 as lite
class main():
    def __init__(self):
        self.x = 1
    def buildMain(self):
        self.root = Tk()
        self.frameOne = Frame(self.root)
        self.frameOne.grid(row=0,column=0)
        self.frameTwo = Frame(self.root)
        self.frameTwo.grid(row=1, column=0)

        #Creating of a new frame, inside of "frameTwo" to the objects to be inserted
        #Creating a scrollbar

        #The reason for this, is to attach the scrollbar to "FrameTwo", and when the size of frame "dataFrame" exceed the size of frameTwo, the scrollbar acts
        self.canvas=Canvas(self.frameTwo)
        self.dataFrame=Frame(self.canvas)
        self.scrollb=Scrollbar(self.root, orient="vertical",command=self.canvas.yview)
        self.scrollb.grid(row=1, column=1, sticky='nsew')  #grid scrollbar in master, but
        self.canvas['yscrollcommand'] = self.scrollb.set   #attach scrollbar to frameTwo

        self.canvas.create_window((0,0),window=self.dataFrame,anchor='nw')
        self.dataFrame.bind("<Configure>", self.AuxscrollFunction)
        self.scrollb.grid_forget()                     #Forget scrollbar because the number of pieces remains undefined by the user. But this not destroy it. It will be "remembered" later.

        self.canvas.grid()

        self.indvidualRunnerStartB = Button(self.frameOne, text = "INDVIUDAL RUNNER", command = self.buildRunnerData)
        self.teamDataButton = Button(self.frameOne,text="TEAM DATA", command=self.buildRunnerData)
        self.indvidualRunnerStartB.grid(row = 7, column = 0, pady=(5,5))
        self.teamDataButton.grid(row=6, column=0, pady=(5,5))
        self.root.mainloop()

    def AuxscrollFunction(self,event):
        #You need to set a max size for frameTwo. Otherwise, it will grow as needed, and scrollbar do not act
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=600,height=500)
    def buildRunnerData(self):



            #IMPORTANT!!! All the objects are now created in "dataFrame" and not in "frameTwo"
            #I perform the alterations. Check it out
        try:
            self.frameOne.grid_forget()
            #val = int(self.entrypiezas.get())
            self.buildRunnerStats()
            self.scrollb.grid(row=1, column=1, sticky='nsew')  #grid scrollbar in master, because user had defined the numer of pieces
        except ValueError:
            showerror('Error', "Introduce un numero")

    def buildRunnerStats(self):
        #self.num_piezas = self.entrypiezas.get()
        dataC = data()
        self.canDb = dataC.openDataBase()
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
                #print(self.output)
                locals()['runnerStat%runner' % self.i] = Label(self.dataFrame, text = self.runnerStats)
                locals()['runnerStat%runner' % self.i].grid(row = self.rowNum)
                self.i = int(self.i) + 1
                self.rowNum = int(self.rowNum) + 1
                #ss

        self.x = 10
        while(self.x!=50):

            locals()['runnerStat%runner' % self.x] = Label(self.dataFrame, text = self.x)
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
                locals()['race%raceId' % self.raceId] = Label(self.dataFrame, text = 'Race'+str(self.raceId)+': '+str(items), borderwidth = 2)
                locals()['race%raceId' % self.raceId].grid(row = self.rowNum, column = self.columnNum )
                self.raceId = self.raceId + 1
                self.columnNum = self.columnNum + 1
        if(self.canDb=='False'):
            print('s')
            #self.failureT2 = Label(self.runnersFrame, text='Failure -- Could not find db, or we has a importation error')
            #self.failureT2.grid()
        print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Build successfull...')
        self.scrollb.grid(sticky = 'ew')



    def addpieza(self):
        self.textopiezanuevo = Label(self.dataFrame, text = "Pieza: ", justify="left")
        self.textopiezanuevo.grid(row=int(self.num_piezas)+1, column=0)

        var = StringVar()
        menu = OptionMenu(self.dataFrame, var, *self.mispiezas)
        menu.grid(row=self.n, column=1)
        menu.config(width=10)
        menu.grid(row=int(self.num_piezas)+1, column=1)
        var.set("One")
        self.optionmenus_piezas.append((menu, var))

        self.numpiezastext = Label(self.dataFrame, text = "Numero de piezas: ", justify="center")
        self.numpiezastext.grid(row=int(self.num_piezas)+1, column=2, padx=(10,0))
        self.entrynumpiezas = Entry(self.dataFrame,width=6)
        self.entrynumpiezas.grid(row=int(self.num_piezas)+1, column=3, padx=(0,10))
        self.entrynumpiezas.insert(0, "0")

        self.textoprioridad = Label(self.dataFrame, text = "Prioridad: ", justify="center")
        self.textoprioridad.grid(row=int(self.num_piezas)+1, column=4)
        var2 = StringVar()
        menu2 = OptionMenu(self.dataFrame, var2, "Normal", "Baja", "Primera pieza", "Esta semana")
        menu2.config(width=10)
        menu2.grid(row=int(self.num_piezas)+1, column=5)
        var2.set("Normal")
        self.optionmenus_prioridad.append((menu2, var2))

        self.lotestext = Label(self.dataFrame, text = "Por lotes?", justify="center")
        self.lotestext.grid(row=int(self.num_piezas)+1, column=6, padx=(10,0))
        self.var1 = IntVar()
        self.entrynumlotes = Checkbutton(self.dataFrame, variable=self.var1)
        self.entrynumlotes.grid(row=int(self.num_piezas)+1, column=7, padx=(5,10))
        self.lotes.append(self.var1)

        self.numpiezas.append(self.entrynumpiezas)
        self.num_piezas = int(self.num_piezas)+1


class data:
	def __init__(self):
		self.x = False
		"""
		Here is where we should bring in our databases, and any other data bases.
		"""

	def openDataBase(self):
		print('['+'\033[31m'+'ProjectRunner'+'\033[0m'+']'+'Attempting to open up the data base...')
		try:

			self.conn = lite.connect('Data/runner.db')
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
			self.conn = lite.connect('Data/runner.db')
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
		self.conn = lite.connect('Data/runner.db')
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
		conn = lite.connect('Data/runner.db')
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
		conn = lite.connect('Data/runner.db')
		c = conn.cursor()
		c.execute("select * from Identification")
		self.data = c.fetchall()
		self.numOfRunners = 0
		for items in self.data:
			self.numOfRunners = self.numOfRunners+1
		return(self.numOfRunners)


main = main()
main.buildMain()
