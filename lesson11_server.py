import socket

sock = socket.socket()

host = '127.0.0.1'
port = 7890

sock.bind((host, port))
sock.listen(1)
print('Listening {0} on port {1}'.format(host, port))

conn, addr = sock.accept()
print('connected: {}'.format(addr))

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()