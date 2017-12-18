"""
Gspread & oauth command/data are commented out for the sake of non internet testing
"""

import sqlite3 as lite
import socket
#import gspread
import json
#from oauth2client.service_account import ServiceAccountCredentials
import xml.etree.cElementTree as Et
"""
TODO:
##Add encryption to the sockets
##Add xml math


class networking:
    def __init__(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind(('127.0.0.1', 80))
            self.s.listen(7)
            self.s.close()
            print('[-- Socket estabished --]')
            print('[-- Socket Library is ready for use: Starting Program--]')
        except:
            print('Couldnt bind a socket to local host on port 80... exiting, please check perms, etc etc then try again...')
            exit()
    def mainNetworking(self):
        host = '127.0.0.1'
        port = 29317
        print('[-- Starting server on IP: '+host+':'+str(port)+' --]')
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        print('[-- Server Started on IP: '+host+':'+str(port)+' --]')
        self.s.listen(10)
        while True:
            cs , addr = self.s.accept()
            print(str(cs)+' '+str(addr))
            self.data = cs.recv(1024).decode()
            if not self.data:
                print('[-- Data given was empty --]')
            if self.data:
                procDataC = procData()
                self.result = procDataC.proccessDbData(self.data)
                self.result = str(self.result)
                #print(self.result) #Maybe return this data to client?
                cs.send(self.result.encode())

class procData:
    def __init__(self):
        """
        Here is where all the data processing and handling will occur
        """
        print('[-- Proc Data Class Called --]')
    def proccessDbData(self, sData):
        """
        sData is the socket data sent by the user
        So the data recived would look like
        command$#$args_@#@_data
        for example
        0xL08$#$john18:jcTeam01_@#@_https://docs.google.com/spreadsheetExampleUrl
        """
        #print(sData)
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
            print('check login -- ')
            for elem in loginData:

                if(elem[0]==username):
                    if(elem[1]==passW):
                        return(True)
                        break #Just in case lol
                    if(elem[1]!=passW):
                        #eturn(False)
                        pass
                if(elem[0]!=username):
                    #return False
                    pass
            return False #If the for loop doesnt break due to a return, the username and pass wasn't there
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
        self.userSS = gs.open_by_url(url)
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
            Et.SubElement(self.runner, "Name", name = str(str(self.runnerData[1])+' '+str(self.runnerData[2])))
            Et.SubElement(self.runner, "Training Data",  meter800 = self.runnerData[3], mile = self.runnerData[4], mile2 = self.runnerData[5], meter500 = self.runnerData[6], meters3000 = self.runnerData[7], meters1500 = self.runnerData[8], meters1600 = self.runnerData[9])
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
        return self.xmlUrl
class mainProg:
    def __init__(self):
        print('[ -- Check Start Up Status --]')
        self.networkingC = networking()
    def mainProg(self):
        print('[-- Project Runner --]')
        print('[-- Server --]')
        """ NO INTERNET -- CAN'T RUN
        authorizationC = authorization()
        if(authorizationC.checkAuth()=='True'):
            pass
        if(authorizationC.checkAuth()=='False'):
            #quit program/ pass the error and start a offline section
            print('[-- Could not connect to Google Sheets, please check the connection of the server... --]')
        """

        self.networkingC.mainNetworking()
class authorization:
    def __init__(self):
        print('[-- Starting Gspread Authorization --]')
        """
        self.authJson  = 'authfile.json'
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.authJson, scope)
        """
    def checkAuth(self):
        global gc
        gc = gspread.authorize(credentials)
        try:
            gc.open_by_url('https://docs.google.com/testspreadsheet')
            #Add a close command here...

            return 'True'
        except:
            return 'False'
mainProgC = mainProg()
mainProgC.mainProg()
