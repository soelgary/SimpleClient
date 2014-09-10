import socket
from optparse import OptionParser

def parse_request(data):
  split_data = data.split(" ")
  print split_data


def main(options, hostname, neu_id):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((hostname, options.port))
  s.listen(1)
  conn, addr = s.accept()
  print 'Connected by', addr
  while 1:
    data = conn.recv(256)
    if data:
      conn.sendall(data)
      parse_request(data)
  conn.close()

parser = OptionParser()

parser.add_option("-p", "--port", dest="port", 
  help="choose a port to connect to", default=27993)
parser.add_option("-s", "--ssl", action="store_true", 
  help="use ssl capabilities", default=False)
(options, args) = parser.parse_args()

hostname = ''
neu_id = ''
try:
  hostname = args[0]
  neu_id = args[1]
except IndexError:
  print 'Incorrect command line arguments. Exiting.'
  exit()
main(options, hostname, neu_id)