import sqlite3 as lite
import os

class vdot:
    def __init__(self):
        pass
    def fetchVdotNum(types, time):
        conn = lite.connect('vdotDb.db')
        c = conn.cursor()
        c.execute("select * from vdot")
        mins, secs = time.split(':')
        time = int(secs) + int(mins) * 60
        data = c.fetchall()
        bigL = []
        x = 0
        for items in data:
            types1 = items[int(types)]
            mins, secs = types1.split(':')
            vdotTime = int(int(mins) * 60) + int(secs)
            vdotNum = str(items[0])
            difference = str(int(vdotTime) - int(time))
            difference = difference.replace('-','')
            listS = [difference, vdotNum]
            bigL.insert(x, listS)
            print("VDOT: "+str(items[0]))
            x = x + 1
        print(bigL)
        try:
            os.remove('vdot.db')
        except:
            pass
        conn = lite.connect('vdot.db')
        c = conn.cursor()
        c.execute("create table data(vdot int, time int)")
        for items in bigL:
            print(items)
            #each item is now a list that contains time and vdot soooo
            c.execute("insert into data(vdot, time) values (?, ?)", (items[1], items[0]) )
        conn.commit()
        c.close()
        #grab Data
        conn = lite.connect('vdot.db')
        c = conn.cursor()
        c.execute('select vdot, time from data order by time asc')
        returnV = c.fetchall()
        return returnV
vdotC = vdot()
x = vdot.fetchVdotNum('1', '5:18')
print(x[0])
