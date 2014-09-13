import socket
from optparse import OptionParser
import ssl

CLASSNAME = 'cs5700fall2014'
HOST = 'cs5700f14.ccs.neu.edu'

def parse_request(data):
  split_data = data.split(" ")
  print split_data
  bye = split_data[2]
  if bye == 'BYE\n':
    return {"end": True, "message": split_data[1]}
  operator = split_data[3]
  number = None
  if operator == '+':
    number = int(split_data[2]) + int(split_data[4])
  elif operator == '-':
    number = int(split_data[2]) - int(split_data[4])
  elif operator == '*':
    number = int(split_data[2]) * int(split_data[4])
  elif operator == '/':
    number = int(split_data[2]) / int(split_data[4])
  return {"end": False, "message": CLASSNAME + ' ' + str(number) + '\n'}

def main(options, hostname, neu_id):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  socket = None
  if options.ssl:
    print 'Using ssl'
    ssl_sock = ssl.wrap_socket(s)
    ssl_sock.connect(('cs5700f14.ccs.neu.edu', 27994))
    socket = ssl_sock
  else:
    s.connect((HOST, options.port))
    socket = s
  s.sendall('cs5700fall2014 HELLO 000507111\n')
  while True:
    data = socket.recv(256)
    parsed = parse_request(data)
    if parsed['end']:
      print parsed['message']
      break
    socket.sendall(parsed['message'])

  s.close()

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