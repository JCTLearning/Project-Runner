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
  VDOT is now calculated. The values are pulled from the SS, and checked against the given mile. We need to pull the VDOT and put it in a db just incase SS fails in the long run. 
  ``` python
  #Ignore incorrect syntax, it is just logic
 	import gspread
	from oauth2client.service_account import ServiceAccountCredentials

	scope = ['https://spreadsheets.google.com/feeds']

	credentials = ServiceAccountCredentials.from_json_keyfile_name('authfile.json', scope)

	gc = gspread.authorize(credentials)
	sheet = '13UTcj1AKMIZ-cCYlKQVIxaYdr8TmOuX43HVw0l0KYmE' # the example sheet king gave
	wks = gc.open_by_key(sheet)
	worksheet = wks.worksheet("VDOT")
	db = []
	vdotNum = 85 # vdot starts on 85 and ends at 30
	loopNum = 0
	for items in worksheet.col_values(4): # the miles column, we can switch this out depending on the data, kek.
    	if(items):
        	if(items=='Mile'): # gets rid of row one -- mile
            	pass
        	else:
            	#print(items) it's just cumbersome.
            	"""
            	convert items into Sec
	    		"""
            	mins, sec = items.split(':')
            	x = int(int(mins)*60) #mins to sec
            	items = int(x) + int(sec) # recompile
            	listV = []
            	listV.insert(0, items)
            	listV.insert(1, vdotNum)
            	db.insert(loopNum, listV) #make it a tup
            	vdotNum = vdotNum - 1
            	loopNum = loopNum + 1
    	else:
        	break
	Vmiles = '224' # User mile speed
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
		#print(output)
	sortedOutput = sorted(output, key = lambda tup: tup[0])
	#print(sortedOutput)
	vdot = sortedOutput[0]
	print(vdot[1])

  ## -- OutPut -- ##
  """
	83 # The VDOT num for the runner according to the miles given.
  """
  ```
