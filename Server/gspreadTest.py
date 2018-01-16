#server
import gspread
from oauth2client.service_account import ServiceAccountCredentials
authJson  = 'authfile.json' # Make sure that is installed.
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(authJson, scope)
gs = gspread.authorize(credentials)
url = 'https://docs.google.com/spreadsheets/d/1lvFMDP6fsuOueuuPx-nJlVGoItWbgUCWGS1eNm2Oys4/edit#gid=0'
userSheet = gs.open_by_url(url)
userSS = userSheet.get_worksheet(0)
print('Value before para saved me: '+str(userSS.row_values(3)))
rowval = userSS.row_values(3)
for x in rowval:
    if(x == ''):
        rowval.remove(x)
print('values after para saved me: '+str(rowval))
