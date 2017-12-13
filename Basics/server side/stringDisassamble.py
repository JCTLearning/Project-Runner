#String unpack example
testString = '0xL08$#$john18:jcTeam01_@#@_https://docs.google.com/spreadsheetExampleUrl'
commandData, data = testString.split('_@#@_')
print(commandData)
print(data)
command, cData = commandData.split('$#$')
print(command)
print(cData)

username, fileName = cData.split(':')
print(username)
print(fileName)
