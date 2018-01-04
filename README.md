# Project-Runner
This is a  program designed to help Track &amp; Cross Country coaches keep track of their stats.
# Progress
  Server side, we still need to test some functions with GSPREAD. Lets first start off with getting gspread to take apart the example spreadsheet. After that the xml data needs to be all put in one node, for example <Runner id='s' name='s'../>, so it's easier to take apart in JS. After that is finished up, on the client side of things, the individual page still needs to be built using XML data. I got a frame work pretty much built. After that the "Check Online" function needs to be built as well. *All it needs todo is ping the server with the Username, and the server will return a string containing all of the available online xml sheet. I'd like to present this option even if there is data on the hard drive.*
# Code setup
  You may need to reorder things, in order for it to work. For example, some scripts use DB folder `data` others use `Data`, note the capital. If the code requires modification, modify it. The only thing that should always be correct is the electron GUI. The server side can be handled.

# Python libs
  ``` python
  #Libs -- client
  import socket
  import sys
  import json
  import os
  import glob
  #Libs -- server
  import sqlite3 as lite
  import socket
  import datetime
  import gspread
  import json
  from oauth2client.service_account import ServiceAccountCredentials
  import xml.etree.cElementTree as Et
  import sys

```

#Electron
  Lets talk about electron shall we?
  Electron displays the data like a webpage, with HTML CSS and JS. The situation is computing lots of data with JS is a lil rough, so what we did was let python handle the data calculation and pass the calculated data back to electron.
  We do this by abusing the python `sys.stdin.readline()` command and the js `exec("py -i pythonClient.py")` command.
  In Java Script we activate the Python program using the exec command, and can pass data to it using the `child.stdin.write()`
  Then in python we capture the data using `sys.stdin.readline()` and compute it. This is equivalent to opening the file in cmd and passing arguments to it. Here when the value is printed though, JS captures said printed data into a var.
  This makes everything 10 times easier with electron. For example the socket connections are easier to handle in python.
  The only issues I have come across is capturing a string output from python and checking it. For example:
  The python program outputs the string 'Db - 0'
  In Js I say `if (pythonVar == 'Db - 0') { runFunct(); }`, the program will never run the function. The string never equals the var, and I can not understand why. The only reason I can think of, is that there is more data inside of the python output, then just 'Db - 0'... Yet when I do console.log(pythonVar) it comes out as 'Db - 0'.
  This presented a major problem. Without these if statements we cant check what python was actually telling us...
  Soooo after toying around a bit, I discovered that JavaScript can recognize python output if its a number. Knowing this, I switched all of my python outputs to either 1 or 0. 1 was false, 0 was true.
  Then by wrapping the python output in `Number()` we can do a if statement to check the outputs.

  As I delve deeper into electron I find that I'm liking it more than tkinter. Although the JS import system is a bit *weird* I suppose there is nothing wrong with it.
