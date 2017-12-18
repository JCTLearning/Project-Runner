import sqlite3 as lite
import xml.etree.cElementTree as Et

"""
DB
"""

root = Et.Element('root')
run = Et.SubElement(root, "Runners")
conn = lite.connect("Data/TeamOne.db")
c = conn.cursor()
c.execute("select * from Identification")
teamData = c.fetchall()
for elem in teamData:
    runnerid = elem[0]
    runnerName = str(elem[1])+str(elem[2])
    Runner = Et.SubElement(run, "ID", id = runnerid )
    Et.SubElement(Runner, "Name", name = runnerName)

"""
XML
"""
tree = Et.ElementTree(root)
tree.write("runner.xml")
