import sqlite3 as lite


class vdot:
    def __init__(self):
        pass
    def fetchVdotNum(self, type, time):
        conn = lite.connect('vdotDb.db')
        c = conn.cursor()
        c.execute("select * from vdot")
        data = c.fetchall()
        for items in data:
            print("num: "+str(items[type]))
            print("VDOT: "+str(items[0]))

vdotC = vdot()
vdot.fetchVdotNum(self, '1', '10:00')
