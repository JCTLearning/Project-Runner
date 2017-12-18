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
  ~~The problem is sort() does "abc order" meaning 123 will be placed after 1000. I doubt anyone will have a 1000 second mile, but it becomes a problem once we get into the 10 min and 20 min range. How else can we order this and hold both the VDOT num and the Mile...~~
  The Problem was solved with the code below. 
  ``` python
  #Ignore incorrect syntax, it is just logic
  db = [('111', '2'), ('334', '1')] # Our vdot list
  Vmiles = '156' # User miles
  output = []
  x = 0
  for miles in db:
	  print(miles)
	  list = []
	  """
	  x is the math
	  """
	  x = int(Vmiles) - int(miles[0])
	  x = str(x)
	  x = x.replace('-', '')
  	print(x)
	  x = int(x)
	  list.insert(0, x)
	  list.insert(1, miles[1])
	  output.insert(x, list)
	  x = x + 1
  print(output)
  sortedOutput = sorted(output, key = lambda tup: tup[0])
  print(sortedOutput)
  vdot = sortedOutput[0]
  print(vdot[1])
  ## -- OutPut -- ##
  """
  ('111', '2')
  45
  ('334', '1')
  178
  [[45, '2'], [178, '1']]
  [[45, '2'], [178, '1']]
  2
  """
  ```
