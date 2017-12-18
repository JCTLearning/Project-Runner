import json
import os
import glob
import sqlite3 as lite
def start():
    print('Starting dbSorter...')
    buildJson()
def buildJson():
    print('Building json file..')


    with open("dbfiles.json", "w") as dbFile:
        json.dump({'dbFiles':'3', '1':'team1.txt', '2':'team2.txt', '3':'team3.txt'}, dbFile, indent=4)
    print("Test data base files added to json.")
    print("Executing data base sort and input.")
    builddB()
def builddB():
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
        print("Done inserting into the list. Avalible dB files are...")
        print(dbList)
        manipdB()
def manipdB():
    print('Manipulating our database files.')
    conn = lite.connect('TeamOne.db')
    c = conn.cursor()
    try:
        c.execute("CREATE TABLE Identification(RunnerID TEXT)")
        c.execute("CREATE TABLE Stats(Race1 TEXT)")
    except lite.Error as e:
        print("Unable to create table because: ")
        print(e)

    a1 = input("[RunnerId]: ")
    a = str(a1)
    b = input("[RunnerName]: ")
    try:
        c.execute("INSERT INTO Identification(RunnerID) VALUES('"+a+"')")
        c.execute("INSERT INTO Stats(Race1) VALUES('"+b+"')")
    except lite.Error as e:
        print("Unable to insert variable into the database because: ")
        print(e)
    try:
        conn.commit()
        c.close()
    except lite.Error as e:
        print(e)

    conn = lite.connect('TeamTwo.db')
    c = conn.cursor()

    d1 = input("[RunnerId]: ")
    d = str(d1)
    f = input("[RunnerName]: ")
    try:
        c.execute("CREATE TABLE Identification(RunnerID TEXT)")
        c.execute("CREATE TABLE Stats(Race1 TEXT)")
    except lite.Error as e:
        print("Unable to create table(s) because: ")
        print(e)

    try:
        c.execute("INSERT INTO Identification(RunnerID) VALUES('"+d+"')")
        c.execute("INSERT INTO Stats(Race1) VALUES('"+f+"')")
    except lite.Error as e:
        print("Unable to insert values into the table because: ")
        print(e)
    try:
        conn.commit()
        c.close()
    except lite.Error as e:
        print(e)
    querydB()
def querydB():
    data1 = ""
    data2 = ""
    data3 = ""
    data4 = ""
    print("Querying database")
    conn = lite.connect('TeamOne.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM Identification")
        set1 = c.fetchall()
        data1 = '\n'.join(elem[0] for elem in set1)
    except lite.Error as e:
        print(e)
    try:
        c.execute("SELECT * FROM Stats")
        set2 = c.fetchall()
        data2 = '\n'.join(elem[0] for elem in set2)
    except lite.Error as e:
        print(e)
    c.close()
    conn = lite.connect('TeamTwo.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM Identification")
        set3 = c.fetchall()
        data3 = '\n'.join(elem[0] for elem in set3)
    except lite.Error as e:
        print(e)
    try:
        c.execute("SELECT * FROM Stats")
        set4 = c.fetchall()
        data4 = '\n'.join(elem[0] for elem in set4)
    except lite.Error as e:
        print(e)


    print('Printing data')
    print('Data Set #1 (File #1 Identification)')
    print(data1)
    print('Data Set #2 (File #1 Stats)')
    print(data2)
    print('Data Set #3(File #2 Identification')
    print(data3)
    print('Data Set (File #2 Stats)')
    print(data4)
        
    
    
    
start()
        
        
        
