import socket, ssl
from optparse import OptionParser

CLASSNAME = 'cs5700fall2014'
DEFAULT_PORT = 27993

# this method accepts the data response from the server, parses it
# and generates a response message and whether or not it is at the end
# of the connection
def parse_request(data):
  split_data = data.split(" ")
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

# this method sets up the connection to the host and handles of sending and 
# recieving all data
def main(options, hostname, neu_id):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  the_socket = None
  if options.ssl:
    ssl_sock = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv3, ca_certs='/etc/ssl/certs/ca-certificates.crt')
    if int(options.port) == 27993:
      ssl_sock.connect((hostname, 27994))
    else:
      ssl_sock.connect((hostname, int(options.port)))
    the_socket = ssl_sock
  else:
    s.connect((hostname, int(options.port)))
    the_socket = s
  the_socket.sendall(CLASSNAME + ' HELLO ' + neu_id + '\n')
  while True:
    data = the_socket.recv(256)
    parsed = parse_request(data)
    if parsed['end']:
      print parsed['message']
      break
    the_socket.sendall(parsed['message'])
  s.close()

# parses the command line args
parser = OptionParser()

parser.add_option("-p", "--port", dest="port", 
  help="choose a port to connect to", default=27993)
parser.add_option("-s", "--ssl", action="store_true", 
  help="use ssl capabilities", default=False)
(options, args) = parser.parse_args()

try:
  main(options, args[0], args[1])
except IndexError:
  print 'Incorrect command line arguments. Exiting.'
  exit()