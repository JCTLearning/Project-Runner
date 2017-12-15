import socket
import gspread 
import json
from oauth2client.service_account import ServiceAccountCredentials
import xml.etree.cElementTree as Et

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
                print(self.result) #Maybe return this data to client?
                cs.send(self.result.encode)
            break
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
        authorizationC = authorization()
        if(authorizationC.checkAuth()=='True'):
            pass
        if(authorizationC.checkAuth()=='False'):
            #quit program/ pass the error and start a offline section
            print('[-- Could not connect to Google Sheets, please check the connection of the server... --]')
        self.networkingC.mainNetworking()
class authorization:
    def __init__(self):
        print('[-- Starting Gspread Authorization --]')

        self.auth = {"type": "service_account","project_id": "pr-testingdata","private_key_id": "612b44bc48ace79cd6afbf0fde56b7423435058b","private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCp76hYLJPQsxDI\njKhXzWm2ZhiO4n9ItNp5XjlM39a5CIIa6NOgSlhMntShy9nj62ENsOfrUkS8XS1Z\nrt7zGHj0zoIwrRYA7jmm/+9vy4DpCwlrCwsFQmBD2BHcZL9apGD3rekjOESebawE\n3kGo16XzTbUsyfffNsWAXMBeT9YIppfMe+w2ox+jIUK3WUzLpx96IwBVZSpNHV21\n/g4PNW+KlmZJgAW152aXOBhI2YuH3fj4AXLqCIHsPD+uxOuQv//qHEGUg8fR0ety\nGCnk9qtFuTxQ98zspKgc8kxSySgJEVE4YeLk6CjP5cQ2XAD4zLl0F7mnJ0eWdenR\nL3KdUsjPAgMBAAECggEACV5R/JJwj7ffe/7tJPIJGuoj/nSUKdD2nmxIYmmQr+C9\nM3iUeii/F3JGLKlNWNhYIGYZUwrVCUFlx6TxW5uEx5I+8SoJpYF8oi1H6PTiJXbb\nTRBtyhtvrS3TRkAzoG6hfeYTjUKD3ewT6KzMF9/ToUcubsqvpJmjZ8E1Rb3HAfD+\nC2IVia3C17BSzP4kZYOhYDSJJVDsjOcetA57wo4Lwn0l7nous4MXNwtTS/gXpgEm\nZMH/dgpAWnxOLpBUzR6yA/n5sKzHGom6YTdFKja/IG8h0CsUgQ04xgNGI+TnbYaP\nlJ04bj6HK/YGe5pOakw6m2n1jWBo2otNmEfS0OBOuQKBgQDtKiijs3j+iNY4coXo\nvguRsAsOnozAmELQKI3iA8R+1eD0gWw4d0JNnPnUJXVV6GeNUKP0DJVf3RVMpyQl\nDpKSpJ5pOV83blk8sv8jZqCHzp+rJ5wK9OEWxPLenglA2XA5dAM+UR1fNRYCceH6\nq0CS/YQ+/uq0bR5IF4eOAhRAfQKBgQC3bqmpUULkRuuQO9THxVVYF8HUiEnckziI\n7zSGYeX4iG5GqEFZWOBH8eo1KruZ4E81mQZT/rODOGoAgGZdZfEekxQnGdocYEt7\nl8xDHH3dPCFF0jbLYdqJiHWar+2nGjtWUeG4zxnVHpaduoBCNCK5cTjJbKZqkJE6\nKhLOhVdcOwKBgAtxT0imrh3JyFws2l0iXjiHP+FSsQPR1NdqPX48JEziUNo7LFeF\nGYPZIQylSgX9EpH05BQwTzyy1AZAwjOvgk7k9mepRvjLsC6HjFvO5cvnojiFzreQ\nnROWKQmoolWoqAt9l3J4Q2yGiStRB1Aq1xDAfpLzhaty4FUmHXoyi3uZAoGAArks\n4auoL5Vx9+E7hn/ChZ1MrmgbmJ/C7h2HDRu0+1yjLn9fAQGVytunm4R35o/y/Ru5\ngVO9vIwA3uMJIgfabZbHbNEwcM1pMXuOd8ybfcZfxBab46cfRH13KYXFJH76NIzg\nqgrBGm3q1IqpTtJRVal9q1fmnJxq2482WkSWiHMCgYAtf5H2mVliIUa6XyHvIj6Q\nZB3JIyJc15sxiB3pVOWIABgnnYa5SPx0m7xRg2WtX1pXoNdYvqzgnt0/+adbcW2/\njWP5gFnsvR0HwPFCuVtueBHERJcmhYUdLz/+7D60Rl9WyX0+1ya8u4yzlLAnsL7M\nVep9m1l1t2+lxmr/rHNvMg==\n-----END PRIVATE KEY-----\n","client_email": "projectrunner-test@pr-testingdata.iam.gserviceaccount.com","client_id": "104879633945044009274","auth_uri": "https://accounts.google.com/o/oauth2/auth","token_uri": "https://accounts.google.com/o/oauth2/token","auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/projectrunner-test%40pr-testingdata.iam.gserviceaccount.com"}
        self.authJson = json.dumps(self.auth)
        print('[-- Using service acct: '+self.authJson[project_id]+' --]')
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.authJson, scope)

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
