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
    def vdotMiles(self, runnerTime, path):
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
                    ##print(items)
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
            ##print(miles)
            ##print('x'+miles[0])
            x, y = miles[0].split(':')
            mileTime = int(x)*60
            mileTime = mileTime + int(y)
            #print('VDOTNUMBER: '+str(miles[1])+' ITS SECONDS: '+str(mileTime))
            list = []
            """
            x is the math
            """
            x = int(Vmiles) - int(mileTime)
            x = str(x)
            x = x.replace('-', '')
            #print('USERTIME: '+str(Vmiles)+' - VDOT SECONDS: '+ str(mileTime)+' THE DISTANCE BETWEEN THE TWO: '+str(x))

            x = int(x)
            list.insert(0, x) #subtracted time
            list.insert(1, miles[1]) #vdot
            output.insert(x, list)
            x = x + 1
        """
        Sorting --  what need to happen here is that each file is deleted upon the script running, but we store the 1500.db in the user fiie. Lets also name it mile or km depending on value.
        """
        conn = lite.connect('tmp/'+path+'miles.db')
        c = conn.cursor()
        c.execute("create table data(vdot int, time int)")
        for items in output:
            #each item is now a list that contains time and vdot soooo
            c.execute("insert into data(vdot, time) values (?, ?)", (items[1], items[0]) )
        conn.commit()
        c.close()
        #grab Data
        conn = lite.connect('tmp/'+path+'miles.db')
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
        #print(vdotNum)
        #print('The VDOT for time: '+str(runnerTime)+' is: '+str(vdotNum[0]))
        """
    def vdot1500(self, runnerTime, path):
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
                if(items=='1500'): # gets rid of row one -- mile
                    pass
                else:
                    ##print(items)
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
            ##print(miles)
            ##print('x'+miles[0])
            x, y = miles[0].split(':')
            mileTime = int(x)*60
            mileTime = mileTime + int(y)
            #print('VDOTNUMBER: '+str(miles[1])+' ITS SECONDS: '+str(mileTime))
            list = []
            """
            x is the math
            """
            x = int(Vmiles) - int(mileTime)
            x = str(x)
            x = x.replace('-', '')
            #print('USERTIME: '+str(Vmiles)+' - VDOT SECONDS: '+ str(mileTime)+' THE DISTANCE BETWEEN THE TWO: '+str(x))
            x = int(x)
            list.insert(0, x) #subtracted time
            list.insert(1, miles[1]) #vdot
            output.insert(x, list)
            x = x + 1
            """
            Sorting --  what need to happen here is that each file is deleted upon the script running, but we store the 1500.db in the user fiie. Lets also name it mile or km depending on value.
            """
        conn = lite.connect('tmp/'+path+'1500.db')
        c = conn.cursor()
        c.execute("create table data(vdot int, time int)")
        for items in output:
            #each item is now a list that contains time and vdot soooo
            c.execute("insert into data(vdot, time) values (?, ?)", (items[1], items[0]) )
        conn.commit()
        c.close()
        #grab Data
        conn = lite.connect('tmp/'+path+'1500.db')
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
        #print(vdotNum)
        #print('The VDOT for time: '+str(runnerTime)+' is: '+str(vdotNum[0]))
        """
    def vdot1600(self, runnerTime, path):
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
                if(items=='1600'): # gets rid of row one -- mile
                    pass
                else:
                    ##print(items)
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
            ##print(miles)
            ##print('x'+miles[0])
            x, y = miles[0].split(':')
            mileTime = int(x)*60
            mileTime = mileTime + int(y)
            #print('VDOTNUMBER: '+str(miles[1])+' ITS SECONDS: '+str(mileTime))
            list = []
            """
            x is the math
            """
            x = int(Vmiles) - int(mileTime)
            x = str(x)
            x = x.replace('-', '')
            #print('USERTIME: '+str(Vmiles)+' - VDOT SECONDS: '+ str(mileTime)+' THE DISTANCE BETWEEN THE TWO: '+str(x))
            x = int(x)
            list.insert(0, x) #subtracted time
            list.insert(1, miles[1]) #vdot
            output.insert(x, list)
            x = x + 1
            """
            Sorting --  what need to happen here is that each file is deleted upon the script running, but we store the 1600.db in the user fiie. Lets also name it mile or km depending on value.
            """
        conn = lite.connect('tmp/'+path+'1600.db')
        c = conn.cursor()
        c.execute("create table data(vdot int, time int)")
        for items in output:
            #each item is now a list that contains time and vdot soooo
            c.execute("insert into data(vdot, time) values (?, ?)", (items[1], items[0]) )
        conn.commit()
        c.close()
        #grab Data
        conn = lite.connect('tmp/'+path+'1600.db')
        c = conn.cursor()
        c.execute('select vdot, time from data order by time asc')
        returnSql = c.fetchall()


        vdot = returnSql[0] #selects     the first value
        return vdot[0] #this is the vdot for that number -- just returns the vdot number
    def vdot3000M(self, runnerTime, path):
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
        for items in worksheet.col_values(5): #4 is miles
            if(items):
                if(items=='3000M'): # gets rid of row one -- mile
                    pass
                else:
                    ##print(items)
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
            ##print(miles)
            ##print('x'+miles[0])
            x, y = miles[0].split(':')
            mileTime = int(x)*60
            mileTime = mileTime + int(y)
            #print('VDOTNUMBER: '+str(miles[1])+' ITS SECONDS: '+str(mileTime))
            list = []
            """
            x is the math
            """
            x = int(Vmiles) - int(mileTime)
            x = str(x)
            x = x.replace('-', '')
            #print('USERTIME: '+str(Vmiles)+' - VDOT SECONDS: '+ str(mileTime)+' THE DISTANCE BETWEEN THE TWO: '+str(x))
            x = int(x)
            list.insert(0, x) #subtracted time
            list.insert(1, miles[1]) #vdot
            output.insert(x, list)
            x = x + 1
            """
            Sorting --  what need to happen here is that each file is deleted upon the script running, but we store the 1600.db in the user fiie. Lets also name it mile or km depending on value.
            """
        conn = lite.connect('tmp/'+path+'3000M.db')
        c = conn.cursor()
        c.execute("create table data(vdot int, time int)")
        for items in output:
            #each item is now a list that contains time and vdot soooo
            c.execute("insert into data(vdot, time) values (?, ?)", (items[1], items[0]) )
        conn.commit()
        c.close()
        #grab Data
        conn = lite.connect('tmp/'+path+'3000M.db')
        c = conn.cursor()
        c.execute('select vdot, time from data order by time asc')
        returnSql = c.fetchall()


        vdot = returnSql[0] #selects     the first value
        return vdot[0] #this is the vdot for that number -- just returns the vdot number
    def vdot3200(self, runnerTime, path):
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
                if(items=='3200'): # gets rid of row one -- mile
                    pass
                else:
                    ##print(items)
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
            ##print(miles)
            #print('error: '+miles[0])
            x, y = miles[0].split(':')
            mileTime = int(x)*60
            mileTime = mileTime + int(y)
            #print('VDOTNUMBER: '+str(miles[1])+' ITS SECONDS: '+str(mileTime))
            list = []
            """
            x is the math
            """
            x = int(Vmiles) - int(mileTime)
            x = str(x)
            x = x.replace('-', '')
            #print('USERTIME: '+str(Vmiles)+' - VDOT SECONDS: '+ str(mileTime)+' THE DISTANCE BETWEEN THE TWO: '+str(x))
            x = int(x)
            list.insert(0, x) #subtracted time
            list.insert(1, miles[1]) #vdot
            output.insert(x, list)
            x = x + 1
            """
            Sorting --  what need to happen here is that each file is deleted upon the script running, but we store the 1600.db in the user fiie. Lets also name it mile or km depending on value.
            """
        conn = lite.connect('tmp/'+path+'3200.db')
        c = conn.cursor()
        c.execute("create table data(vdot int, time int)")
        for items in output:
            #each item is now a list that contains time and vdot soooo
            c.execute("insert into data(vdot, time) values (?, ?)", (items[1], items[0]) )
        conn.commit()
        c.close()
        #grab Data
        conn = lite.connect('tmp/'+path+'3200.db')
        c = conn.cursor()
        c.execute('select vdot, time from data order by time asc')
        returnSql = c.fetchall()


        vdot = returnSql[0] #selects     the first value
        return vdot[0] #this is the vdot for that number -- just returns the vdot number
    def vdotMileTwo(self, runnerTime, path):
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
                if(items=='2 Mile'): # gets rid of row one -- mile
                    pass
                else:
                    ##print(items)
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
            ##print(miles)
            #print('error: '+miles[0])
            x, y = miles[0].split(':')
            mileTime = int(x)*60
            mileTime = mileTime + int(y)
            #print('VDOTNUMBER: '+str(miles[1])+' ITS SECONDS: '+str(mileTime))
            list = []
            """
            x is the math
            """
            x = int(Vmiles) - int(mileTime)
            x = str(x)
            x = x.replace('-', '')
            #print('USERTIME: '+str(Vmiles)+' - VDOT SECONDS: '+ str(mileTime)+' THE DISTANCE BETWEEN THE TWO: '+str(x))
            x = int(x)
            list.insert(0, x) #subtracted time
            list.insert(1, miles[1]) #vdot
            output.insert(x, list)
            x = x + 1
            """
            Sorting --  what need to happen here is that each file is deleted upon the script running, but we store the 1600.db in the user fiie. Lets also name it mile or km depending on value.
            """
        conn = lite.connect('tmp/'+path+'mileTwo.db')
        c = conn.cursor()
        c.execute("create table data(vdot int, time int)")
        for items in output:
            #each item is now a list that contains time and vdot soooo
            c.execute("insert into data(vdot, time) values (?, ?)", (items[1], items[0]) )
        conn.commit()
        c.close()
        #grab Data
        conn = lite.connect('tmp/'+path+'mileTwo.db')
        c = conn.cursor()
        c.execute('select vdot, time from data order by time asc')
        returnSql = c.fetchall()


        vdot = returnSql[0] #selects     the first value
        return vdot[0] #this is the vdot for that number -- just returns the vdot number
    def vdot5000M(self, runnerTime, path):
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
                if(items=='5000M'): # gets rid of row one -- mile
                    pass
                else:
                    ##print(items)
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
            ##print(miles)
            ##print('x'+miles[0])
            x, y = miles[0].split(':')
            mileTime = int(x)*60
            mileTime = mileTime + int(y)
            #print('VDOTNUMBER: '+str(miles[1])+' ITS SECONDS: '+str(mileTime))
            list = []
            """
            x is the math
            """
            x = int(Vmiles) - int(mileTime)
            x = str(x)
            x = x.replace('-', '')
            #print('USERTIME: '+str(Vmiles)+' - VDOT SECONDS: '+ str(mileTime)+' THE DISTANCE BETWEEN THE TWO: '+str(x))
            x = int(x)
            list.insert(0, x) #subtracted time
            list.insert(1, miles[1]) #vdot
            output.insert(x, list)
            x = x + 1
            """
            Sorting --  what need to happen here is that each file is deleted upon the script running, but we store the 1600.db in the user fiie. Lets also name it mile or km depending on value.
            """
        conn = lite.connect('tmp/'+path+'5000m.db')
        c = conn.cursor()
        c.execute("create table data(vdot int, time int)")
        for items in output:
            #each item is now a list that contains time and vdot soooo
            c.execute("insert into data(vdot, time) values (?, ?)", (items[1], items[0]) )
        conn.commit()
        c.close()
        #grab Data
        conn = lite.connect('tmp/'+path+'5000m.db')
        c = conn.cursor()
        c.execute('select vdot, time from data order by time asc')
        returnSql = c.fetchall()


        vdot = returnSql[0] #selects     the first value
        return vdot[0] #this is the vdot for that number -- just returns the vdot number
    def calcAll(self, data, path):
        #Data is the google ss data -- the runners numbers etc etc etc etc etc
        #meter800 = self.runnerData[3], mile = self.runnerData[4], mile2 = self.runnerData[5], meter500 = self.runnerData[6], meters3000 = self.runnerData[7], meters1500 = self.runnerData[8], meters1600 = self.runnerData[9]
        vdotC = vdot()
        try:
            for files in glob.glob('tmp/*.db'):
                os.remove(files)

            os.rmdir('tmp')
            os.mkdir('tmp')
            x = datetime.datetime.time(datetime.datetime.now())
            x = str(x)[:8]
            print(x + '[-- Tmp dir did exsist, refreshing it now --]')
        except:
            x = datetime.datetime.time(datetime.datetime.now())
            x = str(x)[:8]
            print(x + '[-- Tmp dir did not exsist, creating one --]')
            os.mkdir('tmp')
        print('data: '+str(data))
        mileVdot = vdotC.vdotMiles(data[4], path)
        mile2Vdot = vdotC.vdotMileTwo(data[5], path)
        meter5000Vdot = vdotC.vdot5000M(data[6], path)
        meter3000Vdot = vdotC.vdot3000M(data[7], path)
        meter1500 = vdotC.vdot3200(data[8], path)
        meter1600 = vdotC.vdot1600(data[9], path)
        print('m: '+str(mileVdot))

        advVdot = int(mileVdot)+int(mile2Vdot)+int(meter5000Vdot)+int(meter3000Vdot)+int(meter1500)+int(meter1600)
        print(advVdot)
        a = 6
        advVdot = advVdot / a #adv
        advVdot = str(advVdot)
        advVdot, x = advVdot.split('.')
        print(advVdot)
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
        0xL08$#$john18!jcTeam01_@#@_https://docs.google.com/spreadsheetExampleUrl
        """
        #print(sData) for when _@#@_ is tossing errors.
        self.commandData, self.data = sData.split('_@#@_')
        self.command, self.commandArg = self.commandData.split('$#$')
        if(self.command=='0xL08'):
            """
            Here we would path to the db file using self.commandArg, which would hold the username and db title.
            The username would be the folder that the db is held in.
            """
            #print(self.commandArg)
            self.pathToDb, self.fileName = self.commandArg.split('!')
            self.buildData = self.buildDb(self.data, self.fileName, self.pathToDb)
            return self.buildData
        if(self.command=='0xL0S'):
            #Login via sql, weeeeeee
            #split the var up
            #print(self.data)
            username, passW = self.data.split('!')
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
            username, passW = self.data.split('!')
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
            #print(url)
            self.userSheet = gc.open_by_url(url)
            self.userSS = self.userSheet.get_worksheet(0)
        except:
            print(x + '[-- Cred auth failed, check google and see if our api is still up? (Or check the network) --]')
            return 'Server Error -- Could not contact google servers... Check back later, we will hopefully have it fixed!'
        self.dbUrl = str(pathToDb)+'/'+fileName+'.db'
        """
        Open the DB -- And make our tables
        """
        x = datetime.datetime.time(datetime.datetime.now())
        x = str(x)[:8]
        print(x + '[-- Starting to build the db for user: '+str(pathToDb)+' --]')
        self.conn = lite.connect(self.dbUrl) #Creates the file
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE Identification(runnerID TEXT, fname TEXT, lname TEXT)")
        self.c.execute("CREATE TABLE Stats(meter800 TEXT, mile TEXT, mile2 TEXT, meter500 TEXT, meters3000 TEXT, meters1500 TEXT, meters1600 TEXT)")
        """
        Pull the Data from SS -- gonna use a loop and put data in a list
        """
        #count the full row
        x = 0
        y = 1
        z = 1
        while(x!=y):
            if(self.userSS.cell(z,1).value != ''):
                #print('Is full')
                z = z + 1
                pass
            if(self.userSS.cell(z,1).value == ''):
                self.rowCount = z
                #print('isnt full')
                #print(z)
                break


        self.numOfRunners = int(self.rowCount) - 2 #Because the top two rows contain info text
        self.currentRow = 1
        self.rowNum = 3
        self.xmlUrl = str(pathToDb)+'/'+fileName+'.xml' #then we would add this path to our host url for html grab
        self.rootTree = Et.Element('root')
        self.runnerElem = Et.SubElement(self.rootTree, "Runners")
        print('starting runners with data: '+self.xmlUrl)
        isNum = '' #to prevent 'refrence before assignemnt error'
        while(self.currentRow != int(self.numOfRunners + 1 )):
            try:
                print('starting the try')
                data = self.userSS.row_values(self.rowNum)
                print(data)
                secData = data[4]

                x, y = secData.split(':') #fail point
                isNum = 'yes'
            except:
                print('caught the error')
                isNum = 'no'
            if(isNum == 'yes'):
                print('started a runner')
                self.rowval = self.userSS.row_values(self.rowNum)

                for x in self.rowval:
                    if(x == ''):
                        self.rowval.remove(x)

                self.runnerData = self.rowval#self.userSS.row_values(self.rowNum) # THIS WONT WORK: this is a returned value from such a command "['Each row is 1 runner. ## TRAINING DATA', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']"
                """
                xml
                """

                self.runner = Et.SubElement(self.runnerElem, "ID", id = self.runnerData[0])
                #So we decided it was easier just to put all of the data in node for JS. - T
                """
                calc vdot
                """
                vdotC = vdot()
                self.vdotData = vdotC.calcAll(self.runnerData, pathToDb)
                """
                input data into xml
                """
                print('inserting runner:'+ str(self.runnerData[1])+' into xml')
                Et.SubElement(self.runner, "Data", id = self.runnerData[0], name = str(str(self.runnerData[1])+' '+str(self.runnerData[2])), vdotData = self.vdotData, meter800 = self.runnerData[3], mile = self.runnerData[4], mile2 = self.runnerData[5], meter500 = self.runnerData[6], meters3000 = self.runnerData[7], meters1500 = self.runnerData[8], meters1600 = self.runnerData[9])
                """
                Insert into Db
                """
                self.c.execute("insert into Identification (runnerID, fname, lname) values (?, ?, ?)",(self.runnerData[0], self.runnerData[1], self.runnerData[2]))
                self.c.execute("insert into Stats (meter800, mile, mile2, meter500, meters3000, meters1500, meters1600) values (?, ?, ?, ?, ?, ?, ?)", (self.runnerData[3], self.runnerData[4], self.runnerData[5], self.runnerData[6], self.runnerData[7], self.runnerData[8], self.runnerData[9] ))
                self.conn.commit()
                self.currentRow = self.currentRow + 1
                self.rowNum = self.rowNum + 1
                print('finished a runner')
                #End of Loop
            if(isNum != 'yes'):
                print('is not a runner, passing')
                self.currentRow = self.currentRow + 1
                self.rowNum = self.rowNum + 1
                #end of not a number loop
        """
        Clean up and save
        """
        x = datetime.datetime.time(datetime.datetime.now())
        x = str(x)[:8]
        print(x + '[-- cleaning up the xm & db process for user' + pathToDb + ' --]')
        self.tree = Et.ElementTree(self.rootTree)
        self.tree.write(self.xmlUrl) #Xml is written and cleaned up
        self.conn.commit() #Commit to the db -- forgot todo this earlier and the ss were not saving in the db...
        self.c.close() #DB is finished here
        print(self.tree)

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
            #gc.open_by_key('1lvFMDP6fsuOueuuPx-nJlVGoItWbgUCWGS1eNm2Oys4')
            #Add a close command here...

            return 'True'
        except:
            return 'False'
mainProgC = mainProg()
mainProgC.mainProg()
