import socket
from optparse import OptionParser

CLASSNAME = 'cs5700fall2014'
HOST = 'cs5700f14.ccs.neu.edu'

def parse_request(data):
  # need to parse the data
  # then compute math if necessary
  # then build a response message
  split_data = data.split(" ")
  bye = split_data[2]
  print split_data
  if bye == 'BYE':
    print 'THIS IS THE END'
    return {"end": True, "message": ""}
  operator = split_data[3]
  print split_data
  print operator
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

#cs5700fall2014 HELLO [your NEU ID]\n

def main(options, hostname, neu_id):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, options.port))
  s.sendall('cs5700fall2014 HELLO 000507111\n')
  while True:
    data = s.recv(256)
    print 'Received', repr(data)
    parsed = parse_request(data)
    if parsed['end']:
      break
    s.sendall(parsed['message'])

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