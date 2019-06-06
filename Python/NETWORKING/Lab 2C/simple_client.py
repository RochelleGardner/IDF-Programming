import socket

HOST = '127.0.0.1'
PORT = 65432
#msg = b'Hello Server'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(msg)
    data = s.recv(1024)

print('Received: ', data.decode('utf-8'))