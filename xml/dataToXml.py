from xml.etree import ElementTree as xml

tree = xml.parse("file.xml", "w")

xmlRoot = tree.getroot()
child = xml.Element("file")
xmlRoot.append(child)

tree.write("file.xml", "w")
