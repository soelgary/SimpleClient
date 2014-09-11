# Echo client program
import socket
import time

HOST = '127.0.0.1'    # The remote host
PORT = 27993              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('cs5700fall2014 STATUS 4 + 3\n')
print 'Sent cs5700fall2014 STATUS 4 + 3\n'
data = s.recv(256)
print 'Received', repr(data)
#time.sleep(5)
#s.sendall("Herro")
data2 = s.recv(256)
print 'Received', repr(data2)
s.close()

