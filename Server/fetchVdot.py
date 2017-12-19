## -- Fetch Vdot Nums -- #
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('authfile.json', scope)

gc = gspread.authorize(credentials)
sheet = '13UTcj1AKMIZ-cCYlKQVIxaYdr8TmOuX43HVw0l0KYmE'
wks = gc.open_by_key(sheet)
worksheet = wks.worksheet("VDOT")
db = []
vdotNum = 85
loopNum = 0
for items in worksheet.col_values(4):
    if(items):
        if(items=='Mile'): # gets rid of row one -- mile
            pass
        else:
            print(items)
            listV = []
            listV.insert(0, items)
            listV.insert(1, vdotNum)
            db.insert(loopNum, listV)
            vdotNum = vdotNum - 1
            loopNum = loopNum + 1
    else:
        break
print(db)
