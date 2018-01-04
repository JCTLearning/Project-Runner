#TestClient#
import socket
import sys
import json
import os
import glob
class networking:
    def __init__(self):
        pass
    def checkConn(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect(('www.google.com'))
            self.s.close()
            self.onlineNet = True
            try:
                self.s.connect(('127.0.0.1', 29317)) #The server ip, for now its local host.
                self.s.close()
                self.serverConn = True
            except:
                self.serverConn = False
        except:
            self.onlineNet = False
            self.serverConn = False
        self.connList = []
        self.connList.insert(0, self.onlineNet)
        self.connList.insert(1, self.serverConn)
        return self.connList
    def getSpreadSheetXmlUrl(self, xmlUrl, userData):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('127.0.0.1', 29317)) #This needs to change to a static ip when we start hosting
        teamName = userData # just a lil rebrand
        with open(".userData.json", "r") as jsonFile:
            jsonData = json.load(jsonFile)
            user = str(jsonData["username"])

        self.data = '0xL08$#$'+user+':'+teamName+'_@#@_'+xmlUrl.encode()   #https://docs.google.com/spreadsheetExampleUrl'.encode()

        self.s.sendall(self.data)
        rUrl = self.s.recv(1024).decode()
        return rUrl
    def loginSql(self, data):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('127.0.0.1', 29317))
        self.dataString = '0xL0S$#$auth_@#@_'+data.encode()
        self.s.sendall(self.dataString)
        self.result = self.s.recv(1024).decode()
        if(self.result == 'loginTrue'):
            u, p = data.split(':')
            #This is during the result section so ill write the username file here.
            with open(".userData.json", "w") as jsonFile: #with it set to write, the username will be rewritten every time they login.
                json.dump({'username': u}, jsonFile, indent = 4)

        return self.result
    def createAcctSql(self, data):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('127.0.0.1', 29317))
        self.dataString = '0xC0S$#$createAcct_@#@_'+data.encode()
        self.s.sendall(self.dataString)
        self.result = self.s.recv(1024).decode()
        if(str(self.result)=='True'):
            return 'Account already made'
        if(str(self.result)=='Created'):
            return 'Account created'
    def checkforDB(self):
        #This is a hardisk operation idk why im doing it in the networking class lol
        """
        This section is designed to find the runner folder section, and if its there grab the xml files
        If there isnt one, ask to createone or pull one from the server.
        """
        #Check for folder
        cDir = os.getcwd()
        u = " \ "
        u = u.replace(' ', '')

        #Format from \ to / because windows >:C seriously ima kill which ever windows dev decided \ is better than /

        cDirF = cDir.replace(u, '/') # if on any system that uses / for files, this statement'll pass... unless they used \ in a file name... then we're boned.
        xmlFileSys = cDirF+"/runnerData"
        check = os.path.isdir(cDirF+"/runnerData")
        if(check == True):
            #check for any xml files.
            #first change dir lol, it won't work if you're not in the directory.
            os.chdir(xmlFileSys)
            listXml = 0
            for files in glob.glob("*.xml"):
                listXml = listXml + 1
            if(listXml != 0):
                return 0 #True -- The DB is there
            if(listXml == 0):
                try:
                    os.makedirs('runnerData') # Gonna go ahead and make the dir here so we can populate it later.
                except:
                    pass #Meaning the folder is there yet the files arent...
                return 1 # False -- The files and or the folder isnt there

        if(check == False):
            try:
                os.makedirs('runnerData') # Gonna go ahead and make the dir here so we can populate it later.\
                return 1 #False
            except:
                #Meaning the folder is there yet the files arent...
                pass
            return 1 #False
    def listDb(self):
        #Lists xml files in said folder
        cDir = os.getcwd()
        u = " \ "
        u = u.replace(' ', '')

        #Format from \ to / because windows >:C seriously ima kill which ever windows dev decided \ is better than /
        cDirF = cDir.replace(u, '/')
        xmlFileSys = cDirF+"/runnerData"
        os.chdir(xmlFileSys) # change the dir to the folder
        x = ''
        y = 0
        for files in glob.glob('*.xml'):
            #print(files) We cant just print the vars soooooooooo
            x = x + str(files) + ','

            if(files == 'None'):
                print('0')
                return None
        return(x)


class main:
    def __init__(self):
        pass
    def checkInput(self, inputV):
        #First check for server conn
        networkingC = networking()
        self.netStats = networkingC.checkConn()
        """
        if(self.netStats[0]==False):
            return 'N0C0NN-1' #No internet
        if(self.netStats[0]==True):
            if(self.netStats[1]==False):
                return 'NOC0NN-2' #No server connection but connected to internet
            if(self.netStats[1]==True):
                pass #everything is all good, continue
        ## -- For the sake of testing, since I don't have internet ima just hide this till I have access to the outside world kek -- ##
        """
        #At this point we're connected and can check the given input -- This is all the networking
        """
        inputV is gonna be broken down into segments just like the spread sheet above
            inputV = command$#$args
            Command List:
                0xL08 = load data base, via ss
                0xL0G = login via google
                0xL0S = login via project runner
                0xC0S = Create login via project runner
                0xCD8 = Checks for a db folder and files on the hard disk
                0xL0B = Lists xml documents in folder
        """
        self.command, self.commandArgs = inputV.split('$#$')
        if(self.command=='0xL08'):
            self.creds, self.url = self.commandArgs.split('_@#@_')
            return networkingC.getSpreadSheetXmlUrl(self.url, self.creds)
        if(self.command=='0xL0G'):
            return 'Not built yet'
        if(self.command=='0xL0S'):
            #print(self.commandArgs) we comment this out because anythin printed is returned to the client
            #Check for exsisting user:
            #Login
            result = networkingC.loginSql(self.commandArgs)

            #dump the username to a file here
            return result # loginTrue // loginFalse only two options
        if(self.command=='0xC0S'):
            result = networkingC.createAcctSql(self.commandArgs)
            return result #Account already made // Account created only two option
        if(self.command=='0xCD8'):
            result = networkingC.checkforDB()
            return result # dbExistsTrue // dbExistsFalse
        if(self.command == '0xL0B'):
            result = networkingC.listDb()
            return result
"""
#-- Start --#
"""
electronCommand =  sys.stdin.readline()#)raw_input('sys.stdin.readline(): ')
#pass the arg
mainC = main()
returnVar = mainC.checkInput(electronCommand)
if(returnVar != None):
    print(returnVar) # Since the electron program is fetching what is output to the terminal, this is the easiest way to send data back
