import json
import os
import glob
import sqlite3 as lite
def start():
    print("Starting dbSorter . . .")
    buildJson()

def buildJson():
    print("Building JSON file...")

    with open("dbfiles.json", "w") as dbFile:
        json.dump({'dbFiles':'3', '1':'team1.txt', '2':'team2.txt', '3':'team3.txt'}, dbFile, indent=4)

    print('Test data base files added to json')
    print('Executing data base sort and input')
    buildDb()
def buildDb():
    with open("dbfiles.json", "r") as dbFile:
        dbData = json.load(self.dbFile)
        numOfDb = int(dbData["dbFiles"])
        numOfDb = numOfDb + 1
        global dbList
        dbList = []
        x = 1
        while(x!=numOfDb):
            listNum = x-1
            teamId = str(x)
            dbInsert = dbData[teamId]
            dbList.insert(listNum, dbInsert)
            x = x + 1
        print('Done inserting into the list. Avalible dB files are...')
        print(dbList)
def manipDb():
    print("creating our Database file(s) . . . ")
    """
    I'm going to create this using multiple tables
    One database file for a team (2 tables a file)
    I'll make a CLI that takes input and commits for now.
    (Later it will take input from the GUI and any file
    the user wants to use
    """

    """
    CONNECTING:
    Here we're telling the program that we're looking for
    a specific file in the directory. With the variable
    we can manipulate the data. "Cursor" is essentially
    navigation//manipulation
    """
    conn = lite.connect('TeamOne.db')
    c = conn.cursor()
    """
    CREATING:
    Here we create the table names. We're using a try
    and except function to test if the input is
    within the dB file. The params in the () are the 
    variables we have in the table and their input type.
    """
    #Going to make it one param because SCReW thAT?
    try:
        c.execute("CREATE TABLE Identification(RunnerID INT)")
        c.execute("CREATE TABLE stats(Race1 Text)")
    except lite.Error as e:
        print(e)
    a = input("[RunnerId]: ")
    b = input("[RunnerName]: ")
    try:
        c.execute("INSERT INTO Identification(RunnerID INT) VALUES('"+a+"')")
        c.execute("INERT INTO Stats(Race1) VALUES('"+b+"')")
    except lite.Error as e:
        print(e)
    """
    COMMITTING // CLOSING:
    Closing connection to this file so we can connect to another
    one. Saving the information.
    """
    try:
        conn.commit()
        c.close()
    except lite.Error as e:
        print(e)
    print('k')





start()
