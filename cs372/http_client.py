import socket 
import sys


try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print 'Failed to creaste socket. Error code:' + str(msg[0]) + 'Error message:' + msg[1]
	sys.exit();

print 'socket created'

host = 'gaia.cs.umass.edu'

try:
	remote_ip = socket.gethostbyname( host )

except socket.gaierror:
	print 'Hostname could not be resolved. Exiting'
	sys.exit()

print 'IP address of ' + host + ' is ' + remote_ip


getline = 'GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'
port = 80

s.connect( (remote_ip , port) )
s.sendall(getline)

recieve = s.recv(4096)
print 'Recived message:' + recieve

print 'Message length:' + str(len(recieve))

print 'Socket Connected to ' + host + ' on ip ' + remote_ip

s.close()
