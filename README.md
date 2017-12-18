# Project-Runner
This is a  program designed to help Track &amp; Cross Country coaches keep track of their stats.
# Progress
  Server is ready to go for login *and maybe ss data haven't fully tested it*. The client is *almost* done logic wise, should be good to go by tomorrow. Hopefully everything will be good to roll on friday. 
  We also need a way to check if there are teams on server or not. If so put them up on screen, if not present create new team option. 
  Figured out the concept for vdot, check it out below "Node Js Packages"
# Code setup
You may need to reorder things, in order for it to work. For example, some scripts use DB folder `data` others use `Data`, note the capital. If the code requires modification, modify it. The only thing that should always be correct is the electron GUI. The server side can be handled.

# Server
  The server is to take input from the client via a socket on port 29317. Usually in the form of `command$#$user:data@#@_args`. I'm keeping all the data in one string because it's easier to build, and if a fault occurs you don't get bits and pieces of return data.
# Client
  The back end *built in python* is a simple code block designed to take input, proc, and return it. 
# Python libs
  ``` python
  #Libs
  import sys
  import socket
  import sqlite3 as lite
  import gspread
  import zerorpc
  import pyinstaller #pypiwin32 for windows
```

# NodeJS
  ``` javascript
  //NPM Packages
  * Latest version of Electron(1.8.1)
  * Latest version of Mkdirp
```

# Vdot Logic
  The problem is sort() does "abc order" meaning 123 will be placed after 1000. I doubt anyone will have a 1000 second mile, but it becomes a problem once we get into the 10 min and 20 min range. How else can we order this and hold both the VDOT num and the Mile...
  ``` python
  #Ignore incorrect syntax, it is just logic
  calcList = []
  mile = runnerMileNum #like 654 or 700
  vdotList = vdot.getMileList() #List Item will look like ('runnernum', 'vdot')
  for nums in vdotlist:
    vMile = int(nums[0])
    vdotIdent = int(nums[1])
    calc = vMile - mile #Make sure we convert this to positive
    compiledCal = str(calc)+vdotIdent
    calcList.insert(whateverLoopNumWeAreOn, compiledCal)
  #Once loop is done
  calcList = sorted(calcList, key=lambda : [tup: tup[1], int] ) #I have no clue if this will work. We need to sort it by int
  vDot = calcList[0]
  return(vDot)
  ```
