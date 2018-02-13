#Fetch the db file and download data into a table
from oauth2client.service_account import ServiceAccountCredentials
import gspread
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
        x = 1
        y = 58
        while(x!=y):
            for items in worksheet.row_values(x):
                print(items)
            x = x + 1

gdriveC = gdrive()
gdriveC.getValues()
