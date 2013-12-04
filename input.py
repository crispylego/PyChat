import socket

print 'PyChat input window\n===================\n'

HOST = raw_input('Enter server IP: ')
PORT = 1337
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

print '>Sending connection request...'
sock.sendall('request')

data = sock.recv(1024)
if data == 'accepted':
	print '>Connection request accepted.\n'

while 1:
	message = raw_input('Message: ')
	sock.sendall(message)
