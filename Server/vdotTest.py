## -- Fetch Vdot Nums -- #
import sqlite3 as lite
import gspread
from oauth2client.service_account import ServiceAccountCredentials
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
