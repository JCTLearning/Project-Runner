# Project-Runner
This is a  program designed to help Track &amp; Cross Country coaches keep track of their stats.
# Progress
  Server is built (most of it) the only thing that remains is cleaning up and adding SS to it. I need to add in the code for db to xml as well. 
  Electron progress: 
    The program can pull data from XML, it just needs to be neat and clean now... Sockets need to be built as well.
# Code setup
You may need to reorder things, in order for it to work. For example, some scripts use DB folder `data` others use `Data`, note the capital. If the code requires modification, modify it. The only thing that should always be correct is the electron GUI. The server side can be handled.

# Python libs
  ``` python
  #Libs
  import socket
  import sqlite3 as lite
  import gpsread
```

# NodeJS
  ``` javascript
  //NPM Packages
  * Latest version of Electron(1.8.1)
  * Latest version of Mkdirp
```

