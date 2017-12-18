import sqlite3 as lite
#Script to write our test data
conn = lite.connect('test.db')
c = conn.cursor()
def start():
    print("Starting the program that allows you to insert data into a test data base file")
    fileCreation()
def fileCreation():
    print("Creating the database file")
    print("Connected to file")
    c.execute("CREATE TABLE Identificaiton(RunnerID TEXT, RunnerName TEXT)")
    c.execute("CREATE TABLE Stats(Race1 TEXT, Race2 TEXT, Race3 TEXT, Race4 TEXT, Race5)")
    c.execute("CREATE TABLE Team(Avg TEXT)")
    print("Done with file creation")
    fileManipulation()
def fileManipulation():
    #It's a test file you don't need this many damn variables but ok
    print("Starting file manipulation")
    a = str(1)
    b = "John, Rancer"
    c.execute("INSERT INTO Identification(RunnerID, RunnerName) VALUES('"+a+"', '"+b+"')")
    d = "5:50"
    e = "9:50"
    f = "10:30"
    pb = "9:50"
    mile = "9:02"
    c.execute("INSERT INTO Stats(Race1, Race2, Race3, Race4, Race5) VALUES('"+d+"', '"+e+"', '"+f+"', '"+pb+"', '"+mile+"')")
    ravg = "10:02"
    mavg = "8:30"
    c.execute("INSERT INTO Team(Avg) VALUES('"+ravg+"', '"+mavg+"')")
    print("done")
    
    

start()
