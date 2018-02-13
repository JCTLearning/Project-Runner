#Fetch the db file and download data into a table
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import sqlite3 as lite
class gdrive:
    def __init__(self):
        pass
    def getValues(self):
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('authfile.json', scope)
        gc = gspread.authorize(credentials)
        sheet = '13UTcj1AKMIZ-cCYlKQVIxaYdr8TmOuX43HVw0l0KYmE'
        wks = gc.open_by_key(sheet)
        worksheet = wks.worksheet("VDOT")
        conn = lite.connect('vdotDb.db')
        c = conn.cursor()

        c.execute("create table vdot(vdot str, m1500 str, m1600 str, mile str, m3000 str, m3200 str, mile2 str, m5000 str)")

        x = 1
        y = 58
        #values
        while(x!=y):
            data = worksheet.row_values(x)
            if(data[0]=="VDOT"):
                pass
            else:
                vdotNum = data[0]
                data1500 = data[1]
                data1600 = data[2]
                dataMile = data[3]
                data3000M = data[4]
                data3200 = data[5]
                data2mile = data[6]
                data5000 = data[7]
                c.execute("insert into vdot(vdot, m1500, m1600, mile, m3000, m3200, mile2, m5000) values (?, ?, ?, ?, ?, ?, ?, ?)", (vdotNum,data1500,data1600,dataMile,data3000M, data3200 ,data2mile,data5000 ))
                print("VDOT: "+vdotNum+" m1500: "+data1500+" m1600: "+data1600+" Mile: "+dataMile+" m3000: "+data3000M+" m3200"+data3200+" Two Mile: "+data2mile+" m5000: "+data5000)
            x = x + 1
        conn.commit()
gdriveC = gdrive()
gdriveC.getValues()
