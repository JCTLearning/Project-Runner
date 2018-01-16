import sqlite3 as lite
import socket
import datetime
import glob
import os
try:
    import gspread
except:
    x = datetime.datetime.time(datetime.datetime.now())
    x = str(x)[:8]
    print(x + '[-- PLEASE PY -M PIP INSTALL GSPREAD --]')
import json
try:
    from oauth2client.service_account import ServiceAccountCredentials
except:
    x = datetime.datetime.time(datetime.datetime.now())
    x = str(x)[:8]
    print(x + '[-- PLEASE PY -M PIP INSTALL OAUTH --]')
import xml.etree.cElementTree as Et
import sys

"""
TODO:
##Add encryption to the sockets
##Add xml math
NOTE:
##Make sure you change the host IP depending on the server youre hosting on
"""
class vdot:
    def __init__(self):
        print('[-- VDOT CALLED --]')
    def vdotMiles(self, runnerTime):
        x, y = runnerTime.split(':')
        runnerTime = int(x) * 60
        runnerTime = runnerTime + int(y)
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('authfile.json', scope)
        gc = gspread.authorize(credentials)
        sheet = '13UTcj1AKMIZ-cCYlKQVIxaYdr8TmOuX43HVw0l0KYmE'
        wks = gc.open_by_key(sheet)
        worksheet = wks.worksheet("VDOT")
        db = []
        vdotNum = 85
        loopNum = 0
        for items in worksheet.col_values(4): #4 is miles
            if(items):
                if(items=='Mile'): # gets rid of row one -- mile
                    pass
                else:
                    #print(items)
                    listV = []
                    listV.insert(0, items)
                    listV.insert(1, vdotNum)
                    db.insert(loopNum, listV)
                    vdotNum = vdotNum - 1
                    loopNum = loopNum + 1
            else:
                break
        Vmiles = runnerTime # User mile time
        output = []
        x = 0
        for miles in db:
            #print(miles)
            #print('x'+miles[0])
            x, y = miles[0].split(':')
            mileTime = int(x)*60
            mileTime = mileTime + int(y)
            print('VDOTNUMBER: '+str(miles[1])+' ITS SECONDS: '+str(mileTime))
            list = []
            """
            x is the math
            """
            x = int(Vmiles) - int(mileTime)
            x = str(x)
            x = x.replace('-', '')
            print('USERTIME: '+str(Vmiles)+' - VDOT SECONDS: '+ str(mileTime)+' THE DISTANCE BETWEEN THE TWO: '+str(x))

            x = int(x)
            list.insert(0, x) #subtracted time
            list.insert(1, miles[1]) #vdot
            output.insert(x, list)
            x = x + 1
        """
        Sorting --  what need to happen here is that each file is deleted upon the script running, but we store the 1500.db in the user fiie. Lets also name it mile or km depending on value.
        """
        conn = lite.connect('miles.db')
        c = conn.cursor()
        c.execute("create table data(vdot int, time int)")
        for items in output:
            #each item is now a list that contains time and vdot soooo
            c.execute("insert into data(vdot, time) values (?, ?)", (items[1], items[0]) )
        conn.commit()
        c.close()
        #grab Data
        conn = lite.connect('miles.db')
        c = conn.cursor()
        c.execute('select vdot, time from data order by time asc')
        returnSql = c.fetchall()


        vdot = returnSql[0] #selects the first value
        return vdot[0] #this is the vdot for that number -- just returns the vdot number
        """
        runnerTime = input('Mile Time: ')
        x, y = runnerTime.split(':')
        runnerTime = int(x) * 60
        runnerTime = runnerTime + int(y)
        vdotC = vdot()
        selfs = None
        vdotNum = vdot.vdotMiles(selfs, runnerTime)
        print(vdotNum)
        print('The VDOT for time: '+str(runnerTime)+' is: '+str(vdotNum[0]))
        """
    def vdot1500(self, runnerTime):
        x, y = runnerTime.split(':')
        runnerTime = int(x) * 60
        runnerTime = runnerTime + int(y)
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('authfile.json', scope)
        gc = gspread.authorize(credentials)
        sheet = '13UTcj1AKMIZ-cCYlKQVIxaYdr8TmOuX43HVw0l0KYmE'
        wks = gc.open_by_key(sheet)
        worksheet = wks.worksheet("VDOT")
        db = []
        vdotNum = 85
        loopNum = 0
        for items in worksheet.col_values(2): #4 is miles
            if(items):
                if(items=='Mile'): # gets rid of row one -- mile
                    pass
                else:
                    #print(items)
                    listV = []
                    listV.insert(0, items)
                    listV.insert(1, vdotNum)
                    db.insert(loopNum, listV)
                    vdotNum = vdotNum - 1
                    loopNum = loopNum + 1
            else:
                break
        Vmiles = runnerTime # User mile time
        output = []
        x = 0
        for miles in db:
            #print(miles)
            #print('x'+miles[0])
            x, y = miles[0].split(':')
            mileTime = int(x)*60
            mileTime = mileTime + int(y)
            print('VDOTNUMBER: '+str(miles[1])+' ITS SECONDS: '+str(mileTime))
            list = []
            """
            x is the math
            """
            x = int(Vmiles) - int(mileTime)
            x = str(x)
            x = x.replace('-', '')
            print('USERTIME: '+str(Vmiles)+' - VDOT SECONDS: '+ str(mileTime)+' THE DISTANCE BETWEEN THE TWO: '+str(x))
            x = int(x)
            list.insert(0, x) #subtracted time
            list.insert(1, miles[1]) #vdot
            output.insert(x, list)
            x = x + 1
            """
            Sorting --  what need to happen here is that each file is deleted upon the script running, but we store the 1500.db in the user fiie. Lets also name it mile or km depending on value.
            """
        conn = lite.connect('1500.db')
        c = conn.cursor()
        c.execute("create table data(vdot int, time int)")
        for items in output:
            #each item is now a list that contains time and vdot soooo
            c.execute("insert into data(vdot, time) values (?, ?)", (items[1], items[0]) )
        conn.commit()
        c.close()
        #grab Data
        conn = lite.connect('1500.db')
        c = conn.cursor()
        c.execute('select vdot, time from data order by time asc')
        returnSql = c.fetchall()


        vdot = returnSql[0] #selects the first value
        return vdot[0] #this is the vdot for that number -- just returns the vdot number
        """
        runnerTime = input('Mile Time: ')
        x, y = runnerTime.split(':')
        runnerTime = int(x) * 60
        runnerTime = runnerTime + int(y)
        vdotC = vdot()
        selfs = None
        vdotNum = vdot.vdotMiles(selfs, runnerTime)
        print(vdotNum)
        print('The VDOT for time: '+str(runnerTime)+' is: '+str(vdotNum[0]))
        """
    def vdot1600(self, runnerTime):
        x, y = runnerTime.split(':')
        runnerTime = int(x) * 60
        runnerTime = runnerTime + int(y)
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('authfile.json', scope)
        gc = gspread.authorize(credentials)
        sheet = '13UTcj1AKMIZ-cCYlKQVIxaYdr8TmOuX43HVw0l0KYmE'
        wks = gc.open_by_key(sheet)
        worksheet = wks.worksheet("VDOT")
        db = []
        vdotNum = 85
        loopNum = 0
        for items in worksheet.col_values(3): #4 is miles
            if(items):
                if(items=='Mile'): # gets rid of row one -- mile
                    pass
                else:
                    #print(items)
                    listV = []
                    listV.insert(0, items)
                    listV.insert(1, vdotNum)
                    db.insert(loopNum, listV)
                    vdotNum = vdotNum - 1
                    loopNum = loopNum + 1
            else:
                break
        Vmiles = runnerTime # User mile time
        output = []
        x = 0
        for miles in db:
            #print(miles)
            #print('x'+miles[0])
            x, y = miles[0].split(':')
            mileTime = int(x)*60
            mileTime = mileTime + int(y)
            print('VDOTNUMBER: '+str(miles[1])+' ITS SECONDS: '+str(mileTime))
            list = []
            """
            x is the math
            """
            x = int(Vmiles) - int(mileTime)
            x = str(x)
            x = x.replace('-', '')
            print('USERTIME: '+str(Vmiles)+' - VDOT SECONDS: '+ str(mileTime)+' THE DISTANCE BETWEEN THE TWO: '+str(x))
            x = int(x)
            list.insert(0, x) #subtracted time
            list.insert(1, miles[1]) #vdot
            output.insert(x, list)
            x = x + 1
            """
            Sorting --  what need to happen here is that each file is deleted upon the script running, but we store the 1600.db in the user fiie. Lets also name it mile or km depending on value.
            """
        conn = lite.connect('1600.db')
        c = conn.cursor()
        c.execute("create table data(vdot int, time int)")
        for items in output:
            #each item is now a list that contains time and vdot soooo
            c.execute("insert into data(vdot, time) values (?, ?)", (items[1], items[0]) )
        conn.commit()
        c.close()
        #grab Data
        conn = lite.connect('1600.db')
        c = conn.cursor()
        c.execute('select vdot, time from data order by time asc')
        returnSql = c.fetchall()


        vdot = returnSql[0] #selects     the first value
        return vdot[0] #this is the vdot for that number -- just returns the vdot number
    def vdot3000M(self, runnerTime):
        x, y = runnerTime.split(':')
        runnerTime = int(x) * 60
        runnerTime = runnerTime + int(y)
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('authfile.json', scope)
        gc = gspread.authorize(credentials)
        sheet = '13UTcj1AKMIZ-cCYlKQVIxaYdr8TmOuX43HVw0l0KYmE'
        wks = gc.open_by_key(sheet)
        worksheet = wks.worksheet("VDOT")
        db = []
        vdotNum = 85
        loopNum = 0
        for items in worksheet.col_values(3): #4 is miles
            if(items):
                if(items=='Mile'): # gets rid of row one -- mile
                    pass
                else:
                    #print(items)
                    listV = []
                    listV.insert(0, items)
                    listV.insert(1, vdotNum)
                    db.insert(loopNum, listV)
                    vdotNum = vdotNum - 1
                    loopNum = loopNum + 1
            else:
                break
        Vmiles = runnerTime # User mile time
        output = []
        x = 0
        for miles in db:
            #print(miles)
            #print('x'+miles[0])
            x, y = miles[0].split(':')
            mileTime = int(x)*60
            mileTime = mileTime + int(y)
            print('VDOTNUMBER: '+str(miles[1])+' ITS SECONDS: '+str(mileTime))
            list = []
            """
            x is the math
            """
            x = int(Vmiles) - int(mileTime)
            x = str(x)
            x = x.replace('-', '')
            print('USERTIME: '+str(Vmiles)+' - VDOT SECONDS: '+ str(mileTime)+' THE DISTANCE BETWEEN THE TWO: '+str(x))
            x = int(x)
            list.insert(0, x) #subtracted time
            list.insert(1, miles[1]) #vdot
            output.insert(x, list)
            x = x + 1
            """
            Sorting --  what need to happen here is that each file is deleted upon the script running, but we store the 1600.db in the user fiie. Lets also name it mile or km depending on value.
            """
        conn = lite.connect('3000M.db')
        c = conn.cursor()
        c.execute("create table data(vdot int, time int)")
        for items in output:
            #each item is now a list that contains time and vdot soooo
            c.execute("insert into data(vdot, time) values (?, ?)", (items[1], items[0]) )
        conn.commit()
        c.close()
        #grab Data
        conn = lite.connect('3000M.db')
        c = conn.cursor()
        c.execute('select vdot, time from data order by time asc')
        returnSql = c.fetchall()


        vdot = returnSql[0] #selects     the first value
        return vdot[0] #this is the vdot for that number -- just returns the vdot number

    def vdot3200(self, runnerTime):
        x, y = runnerTime.split(':')
        runnerTime = int(x) * 60
        runnerTime = runnerTime + int(y)
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('authfile.json', scope)
        gc = gspread.authorize(credentials)
        sheet = '13UTcj1AKMIZ-cCYlKQVIxaYdr8TmOuX43HVw0l0KYmE'
        wks = gc.open_by_key(sheet)
        worksheet = wks.worksheet("VDOT")
        db = []
        vdotNum = 85
        loopNum = 0
        for items in worksheet.col_values(6): #4 is miles
            if(items):
                if(items=='Mile'): # gets rid of row one -- mile
                    pass
                else:
                    #print(items)
                    listV = []
                    listV.insert(0, items)
                    listV.insert(1, vdotNum)
                    db.insert(loopNum, listV)
                    vdotNum = vdotNum - 1
                    loopNum = loopNum + 1
            else:
                break
        Vmiles = runnerTime # User mile time
        output = []
        x = 0
        for miles in db:
            #print(miles)
            #print('x'+miles[0])
            x, y = miles[0].split(':')
            mileTime = int(x)*60
            mileTime = mileTime + int(y)
            print('VDOTNUMBER: '+str(miles[1])+' ITS SECONDS: '+str(mileTime))
            list = []
            """
            x is the math
            """
            x = int(Vmiles) - int(mileTime)
            x = str(x)
            x = x.replace('-', '')
            print('USERTIME: '+str(Vmiles)+' - VDOT SECONDS: '+ str(mileTime)+' THE DISTANCE BETWEEN THE TWO: '+str(x))
            x = int(x)
            list.insert(0, x) #subtracted time
            list.insert(1, miles[1]) #vdot
            output.insert(x, list)
            x = x + 1
            """
            Sorting --  what need to happen here is that each file is deleted upon the script running, but we store the 1600.db in the user fiie. Lets also name it mile or km depending on value.
            """
        conn = lite.connect('3200.db')
        c = conn.cursor()
        c.execute("create table data(vdot int, time int)")
        for items in output:
            #each item is now a list that contains time and vdot soooo
            c.execute("insert into data(vdot, time) values (?, ?)", (items[1], items[0]) )
        conn.commit()
        c.close()
        #grab Data
        conn = lite.connect('3200.db')
        c = conn.cursor()
        c.execute('select vdot, time from data order by time asc')
        returnSql = c.fetchall()


        vdot = returnSql[0] #selects     the first value
        return vdot[0] #this is the vdot for that number -- just returns the vdot number


    def vdotMileTwo(self, runnerTime):
        x, y = runnerTime.split(':')
        runnerTime = int(x) * 60
        runnerTime = runnerTime + int(y)
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('authfile.json', scope)
        gc = gspread.authorize(credentials)
        sheet = '13UTcj1AKMIZ-cCYlKQVIxaYdr8TmOuX43HVw0l0KYmE'
        wks = gc.open_by_key(sheet)
        worksheet = wks.worksheet("VDOT")
        db = []
        vdotNum = 85
        loopNum = 0
        for items in worksheet.col_values(7): #4 is miles
            if(items):
                if(items=='Mile'): # gets rid of row one -- mile
                    pass
                else:
                    #print(items)
                    listV = []
                    listV.insert(0, items)
                    listV.insert(1, vdotNum)
                    db.insert(loopNum, listV)
                    vdotNum = vdotNum - 1
                    loopNum = loopNum + 1
            else:
                break
        Vmiles = runnerTime # User mile time
        output = []
        x = 0
        for miles in db:
            #print(miles)
            #print('x'+miles[0])
            x, y = miles[0].split(':')
            mileTime = int(x)*60
            mileTime = mileTime + int(y)
            print('VDOTNUMBER: '+str(miles[1])+' ITS SECONDS: '+str(mileTime))
            list = []
            """
            x is the math
            """
            x = int(Vmiles) - int(mileTime)
            x = str(x)
            x = x.replace('-', '')
            print('USERTIME: '+str(Vmiles)+' - VDOT SECONDS: '+ str(mileTime)+' THE DISTANCE BETWEEN THE TWO: '+str(x))
            x = int(x)
            list.insert(0, x) #subtracted time
            list.insert(1, miles[1]) #vdot
            output.insert(x, list)
            x = x + 1
            """
            Sorting --  what need to happen here is that each file is deleted upon the script running, but we store the 1600.db in the user fiie. Lets also name it mile or km depending on value.
            """
        conn = lite.connect('mileTwo.db')
        c = conn.cursor()
        c.execute("create table data(vdot int, time int)")
        for items in output:
            #each item is now a list that contains time and vdot soooo
            c.execute("insert into data(vdot, time) values (?, ?)", (items[1], items[0]) )
        conn.commit()
        c.close()
        #grab Data
        conn = lite.connect('mileTwo.db')
        c = conn.cursor()
        c.execute('select vdot, time from data order by time asc')
        returnSql = c.fetchall()


        vdot = returnSql[0] #selects     the first value
        return vdot[0] #this is the vdot for that number -- just returns the vdot number


    def vdot5000M(self, runnerTime):
        x, y = runnerTime.split(':')
        runnerTime = int(x) * 60
        runnerTime = runnerTime + int(y)
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('authfile.json', scope)
        gc = gspread.authorize(credentials)
        sheet = '13UTcj1AKMIZ-cCYlKQVIxaYdr8TmOuX43HVw0l0KYmE'
        wks = gc.open_by_key(sheet)
        worksheet = wks.worksheet("VDOT")
        db = []
        vdotNum = 85
        loopNum = 0
        for items in worksheet.col_values(8): #4 is miles
            if(items):
                if(items=='Mile'): # gets rid of row one -- mile
                    pass
                else:
                    #print(items)
                    listV = []
                    listV.insert(0, items)
                    listV.insert(1, vdotNum)
                    db.insert(loopNum, listV)
                    vdotNum = vdotNum - 1
                    loopNum = loopNum + 1
            else:
                break
        Vmiles = runnerTime # User mile time
        output = []
        x = 0
        for miles in db:
            #print(miles)
            #print('x'+miles[0])
            x, y = miles[0].split(':')
            mileTime = int(x)*60
            mileTime = mileTime + int(y)
            print('VDOTNUMBER: '+str(miles[1])+' ITS SECONDS: '+str(mileTime))
            list = []
            """
            x is the math
            """
            x = int(Vmiles) - int(mileTime)
            x = str(x)
            x = x.replace('-', '')
            print('USERTIME: '+str(Vmiles)+' - VDOT SECONDS: '+ str(mileTime)+' THE DISTANCE BETWEEN THE TWO: '+str(x))
            x = int(x)
            list.insert(0, x) #subtracted time
            list.insert(1, miles[1]) #vdot
            output.insert(x, list)
            x = x + 1
            """
            Sorting --  what need to happen here is that each file is deleted upon the script running, but we store the 1600.db in the user fiie. Lets also name it mile or km depending on value.
            """
        conn = lite.connect('5000m.db')
        c = conn.cursor()
        c.execute("create table data(vdot int, time int)")
        for items in output:
            #each item is now a list that contains time and vdot soooo
            c.execute("insert into data(vdot, time) values (?, ?)", (items[1], items[0]) )
        conn.commit()
        c.close()
        #grab Data
        conn = lite.connect('5000m.db')
        c = conn.cursor()
        c.execute('select vdot, time from data order by time asc')
        returnSql = c.fetchall()


        vdot = returnSql[0] #selects     the first value
        return vdot[0] #this is the vdot for that number -- just returns the vdot number
    def calcAll(self, data):
        #Data is the google ss data -- the runners numbers etc etc etc etc etc
        #meter800 = self.runnerData[3], mile = self.runnerData[4], mile2 = self.runnerData[5], meter500 = self.runnerData[6], meters3000 = self.runnerData[7], meters1500 = self.runnerData[8], meters1600 = self.runnerData[9]
        vdotC = vdot()
        mileVdot = vdotC.vdotMiles(self.runnerData[4])
        mile2Vdot = vdotC.vdotMileTwo(self.runnerData[5])
        meter5000Vdot = vdotC.vdot5000M(self.runnerData[6])
        meter3000Vdot = vdotC.vdot3000M(self.runnerData[7])
        meter1500 = vdotC.vdot3200(self.runnerData[8])
        meter1600 = vdotC.vdot1600(self.runnerData[9])
        advVdot = int(mileVdot)+int(mile2Vdot)+int(meter5000Vdot)+int(meter3000Vdot)+int(meter1500)+int(meter1600)
        advVdot = advVdot % 6 #adv
        return advVdot
class networking:
    def __init__(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind(('127.0.0.1', 80))
            self.s.listen(7)
            self.s.close()
            x = datetime.datetime.time(datetime.datetime.now())
            x = str(x)[:8]
            print(x+'[-- Socket estabished --]')
            x = datetime.datetime.time(datetime.datetime.now())
            x = str(x)[:8]
            print(x+'[-- Socket Library is ready for use: Starting Program--]')
        except:
            x = datetime.datetime.time(datetime.datetime.now())
            x = str(x)[:8]
            print(x+ 'Couldnt bind a socket to local host on port 80... exiting, please check perms, etc etc then try again...')
            exit()
    def mainNetworking(self):
        host = '127.0.0.1'
        port = 29317
        x = datetime.datetime.time(datetime.datetime.now())
        x = str(x)[:8]
        print(x + '[-- Starting server on IP: '+host+':'+str(port)+' --]')
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        x = datetime.datetime.time(datetime.datetime.now())
        x = str(x)[:8]
        print(x + '[-- Server Started on IP: '+host+':'+str(port)+' --]')
        self.s.listen(10)
        while True:
            cs , addr = self.s.accept()
            self.ip = addr
            x = datetime.datetime.time(datetime.datetime.now())
            x = str(x)[:8]

            print(x +'[-- Connection from: '+str(cs)+' '+str(addr))
            self.data = cs.recv(1024).decode()
            if not self.data:
                x = datetime.datetime.time(datetime.datetime.now())
                x = str(x)[:8]
                print(x+ '[-- Data given was empty --]')
            if self.data:
                procDataC = procData()
                self.result = procDataC.proccessDbData(self.data, self.ip)
                self.result = str(self.result)
                print(self.result)
                #print(self.result) #Maybe return this data to client?
                cs.send(self.result.encode())

class procData:
    def __init__(self):
        """
        Here is where all the data processing and handling will occur
        """
        x = datetime.datetime.time(datetime.datetime.now())
        x = str(x)[:8]
        print(x + '[-- Proc Data Class Called --]')
    def proccessDbData(self, sData, ip):
        """
        sData is the socket data sent by the user
        So the data recived would look like
        command$#$args_@#@_data
        for example
        0xL08$#$john18:jcTeam01_@#@_https://docs.google.com/spreadsheetExampleUrl
        """
        #print(sData) for when _@#@_ is tossing errors.
        self.commandData, self.data = sData.split('_@#@_')
        self.command, self.commandArg = self.commandData.split('$#$')
        if(self.command=='0xL08'):
            """
            Here we would path to the db file using self.commandArg, which would hold the username and db title.
            The username would be the folder that the db is held in.
            """
            self.pathToDb, self.fileName = self.commandArg.split(':')
            self.buildData = self.buildDb(self.data, self.fileName, self.pathToDb)
            return self.buildData
        if(self.command=='0xL0S'):
            #Login via sql, weeeeeee
            #split the var up
            username, passW = self.data.split(':')
            self.conn = lite.connect('authDb.db')
            self.c = self.conn.cursor()
            self.c.execute('select * from auth')
            """
            column 1 is useremail
            column 2 is user pass #needs encryption

            """
            loginData = self.c.fetchall()
            #print(loginData)
            #print('check login -- ')
            for elem in loginData:

                if(elem[0]==username):
                    if(elem[1]==passW):
                        x = datetime.datetime.time(datetime.datetime.now())
                        x = str(x)[:8]
                        print(x + '[--User at: '+str(ip)+' Succeeded to login --]')
                        return(0)
                        break #Just in case lol
                    if(elem[1]!=passW):
                        #eturn(False)
                        pass
                if(elem[0]!=username):
                    #return False
                    pass
            x = datetime.datetime.time(datetime.datetime.now())
            x = str(x)[:8]
            print(x + '[-- User at: '+str(ip)+' Failed to login --]')
            return 1 #If the for loop doesnt break due to a return, the username and pass wasn't there
        if(self.command=='0xC0S'):
            #print(self.commandData)
            username, passW = self.data.split(':')
            self.passW = passW
            self.username = username # I defined weird below, so this fixes it, its only 18 or so bytes of data :shrug:
            self.conn = lite.connect('authDb.db')
            self.c = self.conn.cursor()
            try: #Try and make the table

                self.c.execute("create table auth(useremail TEXT, password TEXT)")
                #Table is made
                pass
            except:
                #Table is made
                pass
            #Check for email in the db to see if it's already used
            self.c.execute('select * from auth')
            self.loginData = self.c.fetchall()
            for userData in self.loginData:
                if(userData[0]==username):
                    #UserAlready has acct
                    return True #should break if user has an account with said email
                pass
            #user does not have an account

            self.c.execute('insert into auth(useremail, password) values (?, ?)', (self.username, self.passW) )
            self.conn.commit()
            self.c.close()
            return 'Created' #User accout is made, but I want to add a email func to this, where we email the user a code, just to make sure the email is right.
        if(self.command=='0xG08'):
            """
            Here is where we would fetch all the xml data for a user and return it in one string
            """

            cDir = os.getcwd()
            u = " \ "
            u = u.replace(' ', '')

            #Format from \ to / because windows >:C seriously ima kill which ever windows dev decided \ is better than /
            cDirF = cDir.replace(u, '/')
            xmlFileSys = cDirF+"/"+self.commandArg

            userFiles = '' #What i can do here is just make a manifest.json for each users and pull data from that instead...
            fileCounter = 0
            for files in glob.glob(self.commandArg+'/*.xml'):
                userFiles = userFiles+ str(files)+','
                fileCounter = fileCounter + 1
            #now all the data is inside userFiles, keep in mind there is an extra comma at the end :/
            x = datetime.datetime.time(datetime.datetime.now())
            x = str(x)[:8]
            print(x + '[-- User: '+str(self.commandArg)+' has '+str(fileCounter)+' xml sheets, sending that data back to them now --]')
            if(fileCounter == 0):
                userFiles = 'False'
                return str(userFiles)
            if(fileCounter != 0):
                userFiles = userFiles.replace(self.commandArg,  '')
                userFiles = userFiles.replace(u, '')
                return str(userFiles)

    def buildDb(self, url, fileName, pathToDb):
        """
        Here we would take the SS url and unpack the data and toss it into a db, then toss it into a xml docs
        After that we would return the xml url
        """
        """
        First we need to make the dir :P
        """
        try:
            x = datetime.datetime.time(datetime.datetime.now())
            x = str(x)[:8]
            os.makedirs(pathToDb)
            print(x + '[-- Created path for '+pathToDb+' --]')
        except:
            print(x + '[-- Path was already made for user, continuing --]')
        try:
            self.authJson  = 'authfile.json' # Make sure that is installed.
            scope = ['https://spreadsheets.google.com/feeds']
            credentials = ServiceAccountCredentials.from_json_keyfile_name(self.authJson, scope)
        except:
            x = datetime.datetime.time(datetime.datetime.now())
            x = str(x)[:8]
            print(x + '[-- OAUTH is not installed smh install it already. --]')
            return 'Server Error -- Could not contact google servers... Check back later, we will hopefully have it fixed!'
        try:
            x = datetime.datetime.time(datetime.datetime.now())
            x = str(x)[:8]
            print(x+ '[-- Trying to authorize our creds --]')
            gc = gspread.authorize(credentials)
            self.userSS = gs.open_by_key('1lvFMDP6fsuOueuuPx-nJlVGoItWbgUCWGS1eNm2Oys4')
        except:
            print(x + '[-- Cred auth failed, check google and see if our api is still up? (Or check the network) --]')
            return 'Server Error -- Could not contact google servers... Check back later, we will hopefully have it fixed!'
        self.dbUrl = str(pathToDb)+'/'+fileName+'.db'
        """
        Open the DB -- And make our tables
        """
        self.conn = lite.connect(self.dbUrl) #Creates the file
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE Identification(runnerID TEXT, fname TEXT, lname TEXT)")
        self.c.execute("CREATE TABLE Stats(meter800 TEXT, mile TEXT, 2mile TEXT, 500meter TEXT, meters3000 TEXT, meters1500 TEXT, meters1600 TEXT)")
        """
        Pull the Data from SS -- gonna use a loop and put data in a list
        """
        self.numOfRunners = int(self.userSS.row_count) - 2 #Because the top two rows contain info text
        self.currentRow = 1
        self.rowNum = 3
        self.xmlUrl = str(pathToDb)+'/'+fileName+'.xml' #then we would add this path to our host url for html grab
        self.rootTree = Et.Element('root')
        self.runnerElem = Et.SubElement(self.rootTree, "Runners")

        while(self.currentRow != int(self.numOfRunners + 1 )):
            self.runnerData = self.userSS.row_values(self.rowNum)
            """
            xml
            """

            self.runner = Et.SubElement(self.runnerElem, "ID", id = self.runnerData[0])
            #So we decided it was easier just to put all of the data in node for JS. - T
            """
            calc vdot
            """
            vdotC = vdot()
            vdotC.calcAll(self.runnerData)
            """
            input data into xml
            """
            Et.SubElement(self.runner, "Data", id = self.runnerData[0], name = str(str(self.runnerData[1])+' '+str(self.runnerData[2])),  meter800 = self.runnerData[3], mile = self.runnerData[4], mile2 = self.runnerData[5], meter500 = self.runnerData[6], meters3000 = self.runnerData[7], meters1500 = self.runnerData[8], meters1600 = self.runnerData[9])
            """
            Insert into Db
            """
            self.c.execute("insert into Identification (runnerID, fname, lname) values (?, ?, ?)",(self.runnerData[0], self.runnerData[1], self.runnerData[2]))
            self.c.execute("insert into Stats (meter800, mile, mile2, 500meter, meters3000, meters1500, meters1600) values (?, ?, ?, ?, ?, ?, ?)", (self.runnerData[3], self.runnerData[4], self.runnerData[5], self.runnerData[6], self.runnerData[7], self.runnerData[8], self.runnerData[9] ))
            self.conn.commit()
            self.currentRow = self.currentRow + 1
            self.rowNum = self.rowNum + 1
            #End of Loop

        """
        Clean up and save
        """
        self.tree = Et.ElementTree(self.rootTree)
        self.tree.write(self.xmlUrl) #Xml is written and cleaned up
        self.conn.commit() #Commit to the db -- forgot todo this earlier and the ss were not saving in the db...
        self.c.close() #DB is finished here


        #Before returning it, I would make it a url for the client to grab, maybe for now we just point at local host, but idk.
        x = datetime.datetime.time(datetime.datetime.now())
        x = str(x)[:8]
        print(x + '[-- Finished up the xm & db process for user' + pathToDb + ' --]')
        return self.xmlUrl

class mainProg:
    def __init__(self):
        x = datetime.datetime.time(datetime.datetime.now())
        x = str(x)[:8]
        print(x + '[ -- Check Start Up Status --]')
        self.networkingC = networking()
    def mainProg(self):
        x = datetime.datetime.time(datetime.datetime.now())
        x = str(x)[:8]
        print(x + '[-- Project Runner --]')
        print(x + '[-- Server --]')

        authorizationC = authorization()
        if(authorizationC.checkAuth()=='True'):
            pass
        if(authorizationC.checkAuth()=='False'):
            #quit program/ pass the error and start a offline section
            x = datetime.datetime.time(datetime.datetime.now())
            x = str(x)[:8]
            print(x + '[-- Could not connect to Google Sheets, please check the connection of the server... --]')
            pass
            #We pass here because this will always be false when I dont have internet :feelsbadman:
        self.networkingC.mainNetworking()
class authorization:
    def __init__(self):
        x = datetime.datetime.time(datetime.datetime.now())
        x = str(x)[:8]
        print(x + '[-- Auth class called --]')
    def checkAuth(self):
        x = datetime.datetime.time(datetime.datetime.now())
        x = str(x)[:8]
        print(x + '[-- Starting Gspread Authorization --]')
        try:
            self.authJson  = 'authfile.json'
            scope = ['https://spreadsheets.google.com/feeds']
            credentials = ServiceAccountCredentials.from_json_keyfile_name(self.authJson, scope)

            global gc
            gc = gspread.authorize(credentials)
        except:
            x = datetime.datetime.time(datetime.datetime.now())
            x = str(x)[:8]
            print(x + '[-- Error: NameError -- OAUTH ISNT installed. If error isnt NameError it is: '+str(sys.exc_info()[0])+' Passing --]')

        try:
            gc.open_by_key('1lvFMDP6fsuOueuuPx-nJlVGoItWbgUCWGS1eNm2Oys4')
            #Add a close command here...

            return 'True'
        except:
            return 'False'
mainProgC = mainProg()
mainProgC.mainProg()
