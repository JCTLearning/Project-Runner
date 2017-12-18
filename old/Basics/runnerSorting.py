import json
import sqlite3 as lite



def start():
    print("Starting algorithim")
    uI()

    
    
def uI():
    print("Running user input functipn")
    data = []
    isDone = False
    while(isDone == False):
        riD = input('[RunnerId]: ')
        data.append(riD)
        z = input("Are you done?")
        if (z == "Y"):
            isDone = True
    print(data)

    print("Finished User Input")
    control()
def control():
    print("Starting control")
    





start()
