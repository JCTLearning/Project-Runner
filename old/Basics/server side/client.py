#TestClient#
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 29317))
data = '0xL08$#$john18:jcTeam01_@#@_https://docs.google.com/spreadsheetExampleUrl'.encode()

s.sendall(data)
x = s.recv(1024).decode()
print(x)
