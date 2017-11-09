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
        dbData = json.load(dbFile)
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
        manipDb()
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
        c.execute("CREATE TABLE Identification(RunnerID TEXT)")
        c.execute("CREATE TABLE Stats(Race1 Text)")
    except lite.Error as e:
        print(e)
    a1 = input("[RunnerId]: ")
    a = str(a1)
    b = input("[RunnerName]: ")
    try:
        
        c.execute("INSERT INTO Identification(RunnerID) VALUES('"+a+"')")
        print("Inserted values into Identification")
        c.execute("INSERT INTO Stats(Race1) VALUES('"+b+"')")
        print("Inserted values into Stats")
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
    conn = lite.connect('TeamTwo.db')
    c = conn.cursor()
    try:
        c.execute("CREATE TABLE Identification(RunnerID TEXT)")
        c.execute("CREATE TABLE Stats(Race1 TEXT)")
    except lite.Error as e:
        print(e)

    c1 = input("[RunnerId]: ")
    c2 = str(c1)
    d = input("[RunnerName]: ")

    try:
        c.execute("INSERT INTO Identification(RunnerID) VALUES('"+c2+"')")
        print("Inserted values into Identification")
        c.execute("INSERT INTO Stats(Race1) VALUES ('"+d+"')")
        print("Inserted values into Stats")
    except lite.Error as e:
        print(e)
    try:
        conn.commit()
        c.close()
    except lite.Error as e:
        print(e)
    querydB()
def querydB():
    data = []
    dataS = []
    sData1 = ""
    sData = ""
    fData = ""
    fData1 = ""
    print("Querying database")
    """
    QUERYING:
    Here we are essentially fetching all data set from the table and putting
    them in a data list we can manipulate. You can also use fetchone() to fetch
    a specific data set.
    """
    conn = lite.connect('TeamOne.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM Identification")
        data = c.fetchall()
        fData = '\n'.join(elem[0] for elem in data)
    except lite.Error as e:
        print(e)
    try:
        c.execute("SELECT * FROM Stats")
        data1 = c.fetchall()
        fData1 = '\n'.join(elem[0] for elem in data)
    except lite.Error as e:
        print(e)
    print("Printing stats table...")
    print(fData1)
    print("Printing identification table...")
    print(fData)
    c.close()
    conn = lite.connect('TeamTwo.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM Identification")
        dataS = c.fetchall()
        sData = '\n'.join(elem[0] for elem in dataS)
    except lite.Error as e:
        print(e)
    try:
        c.execute("SELECT * FROM Stats")
        data2 = c.fetchall()
        sData1 = '\n'.join(elem[0] for elem in data)
    except lite.Error as e:
        print(e)
    c.close()
    print("Printing stats table....")
    print(sData1)
    print("Prnting identification table..")
    print(sData)
    print("Done querying")
        
    

"""
Minor issue -
Not inserting text values into the database file
I added print functions to test if the data inserts right.
It returns. It has to be an error with the table creation (doesn't
create both columns properly)
"""
        
    





start()
