#TestClient#
import socket
import sys
import json
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
        user, teamName = self.userData.split(':')
        self.data = '0xL08$#$'+user+':'+teamName+'_@#@_'+xmlUrl.encode()   #https://docs.google.com/spreadsheetExampleUrl'.encode()

        self.s.sendall(self.data)
        rUrl = s.recv(1024).decode()
        return rUrl
    def loginSql(self, data):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('127.0.0.1', 29317))
        self.dataString = '0xL0S$#$auth_@#@_'+data.encode()
        self.s.sendall(self.dataString)
        self.result = self.s.recv(1024).decode()
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

        """
        self.command, self.commandArgs = inputV.split('$#$')
        if(self.command=='0xL08'):
            self.creds, self.url = self.commandArgs.split('_@#@_')
            return networkingC.getSpreadSheetXmlUrl(self.url, self.creds)
        if(self.command=='0xL0G'):
            return 'Not built yet'
        if(self.command=='0xL0S'):
            print(self.commandArgs)
            #Check for exsisting user:
            #Login
            result = networkingC.loginSql(self.commandArgs)

            #dump the username to a file here
            return result # True // False only two options
        if(self.command=='0xC0S'):
            result = networkingC.createAcctSql(self.commandArgs)
            return result #Account already made // Account created only two option

"""
#-- Start --#
"""
electronCommand = sys.stdin.readline() #raw_input('sys.stdin.readline(): ')
#pass the arg
mainC = main()
returnVar = mainC.checkInput(electronCommand)
print(returnVar) # Since the electron program is fetching what is output to the terminal, this is the easiest way to send data back
