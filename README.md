# Project-Runner
This is a  program designed to help Track &amp; Cross Country coaches keep track of their stats.
# Progress
 The program is done for the most part. As of now we're just doing basic design and bug testing... So that leaves us with what now? Of course we're moving on to diffrent tasks as we move through the year but I think PR has great potential. The program can extend past just a data display tool and vdot calculator to things much better. I only hope that we get the time to acomplish such.
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
  import requests
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
