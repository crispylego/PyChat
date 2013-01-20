import socket

print 'PyChat output window\n====================\n'

HOST = ''
PORT = 31337
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
print 'Server started on port', PORT, '\n'

while 1:
	sock.listen(1)
	conn, addr = sock.accept()
	print 'Connection from', addr
	while 1:
		data = conn.recv(1024)
		if not data: break
		if data == 'request':
			conn.sendall('accepted')
			print 'Accepted request\n'
		else:
			conn.sendall('denied')
			print 'Denied request\n'
		break

	while 1:
		message = conn.recv(1024)
		if not message: break
		print 'Message from', addr, message