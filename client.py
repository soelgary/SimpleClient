# Echo client program
import socket
import time

HOST = '127.0.0.1'    # The remote host
PORT = 27993              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Hello, world')
data = s.recv(256)
time.sleep(5)
s.sendall("Herro")
data2 = s.recv(256)
s.close()
print 'Received', repr(data)
print 'Received', repr(data2)