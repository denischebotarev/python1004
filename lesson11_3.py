import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created')

host = 'google.com'
port = 80

remote_ip = socket.gethostbyname(host)
sock.connect((remote_ip, port))
print('Socket connected to {} on ip {}'.format(host, remote_ip))

message = 'GET / HTTP/1.1\n\r\n\r'
sock.sendall(message.encode('UTF-8'))
print('Message sent succesfully')

reply = sock.recv(4096)
print('Response')
print(reply.decode('UTF-8'))