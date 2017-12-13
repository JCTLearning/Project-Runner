import socket
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
        #build db off of spreadsheet -- url
        #build xml off of db
        self.dbUrl = str(pathToDb)+'/'+fileName+'.db'
        self.xmlUrl = str(pathToDb)+'/'+fileName+'.xml' #then we would add this path to our host url for html grab
        return self.xmlUrl
class mainProg:
    def __init__(self):
        print('[ -- Check Start Up Status --]')
        self.networkingC = networking()

    def mainProg(self):
        print('[-- Project Runner --]')
        print('[-- Server --]')


        self.networkingC.mainNetworking()


mainProgC = mainProg()
mainProgC.mainProg()
