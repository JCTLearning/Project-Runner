import sqlite3 as lite
import socket
import datetime
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
            self.userSS = gs.open_by_url(url)
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
            gc.open_by_url('https://docs.google.com/testspreadsheet')
            #Add a close command here...

            return 'True'
        except:
            return 'False'
mainProgC = mainProg()
mainProgC.mainProg()
