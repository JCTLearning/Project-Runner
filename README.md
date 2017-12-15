# Project-Runner
This is a  program designed to help Track &amp; Cross Country coaches keep track of their stats.
# Progress
  Server is built (most of it) the only thing that remains is cleaning up and fixing authorization via JSON file
  We're looking to using python for the back end of the client side, and electron for the front using a new library we found online, example [here](https://github.com/fyears/electron-python-example/blob/master)
  If we do that, XML client side will be easier, and we'll be able to save copies of SS offline. 
  What I would like todo is reorder the GITHUB page, and get rid of any .py files we're not using. We'll prolly end up just creating a new version.
  As for the GUI, by january, I want to be able to import SS, port them to xml and display their data neatly in the gui. After that is done (this is optional) but we need a way to sign in. Maybe here we can use a sql section for logins, or perhaps we can use google to handle auth...
# Code setup
You may need to reorder things, in order for it to work. For example, some scripts use DB folder `data` others use `Data`, note the capital. If the code requires modification, modify it. The only thing that should always be correct is the electron GUI. The server side can be handled.

# Python libs
  ``` python
  #Libs
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

