import socket

print 'PyChat input window\n===================\n'

HOST = raw_input('Enter host IP: ')
PORT = 31337
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

print '>Sending request...'
sock.sendall('request')

data = sock.recv(1024)
if data == 'accepted':
	print '>Connection accepted.'

while 1:
	message = raw_input('Enter message to send: ')
	sock.sendall(message)