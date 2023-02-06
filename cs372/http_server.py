import socket
import sys

HOST = '127.0.0.1'
PORT = 1025

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Created'


try:
	s.bind((HOST,PORT))
except socket.error, msg:
	print 'Bind failed. Error Code: ' + str(msg[0]) + 'Message: ' + str(msg[1])
	sys.exit()


print 'Socket Bind Compplete'

s.listen(10)
print 'Socket now listening'


conn, addr = s.accept()

print 'Connected with ' + addr[0] + ':' + str(addr[1])


data = """HTTP/1.1 200 OK\r\n\
	Content-Type: text/html; charset=UTF-8\r\n\r\n\
	<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"""
conn.sendall(data)

con.close()
s.close()
