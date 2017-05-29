import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

host = '127.0.0.1'
port = 7890

sock.connect((host,port))
print('Socket connected to {0} on {1}'.format(host, port))

message = input('Enter message: ')
sock.sendall(message.encode('UTF-8'))
print('Message "{}" send succesfully!'.format(message))

data = sock.recv(1024)
print('Response: {}'.format(data.decode('UTF-8')))

sock.close()