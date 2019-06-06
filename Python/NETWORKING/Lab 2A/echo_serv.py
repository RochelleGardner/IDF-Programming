#! /usr/bin/env python3

import socket 

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    # by using with there's no need to close the socket
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print("Client sent: ", data.decode())
            data = data[::-1]  # reverse that string
            if not data:        # if no data then get outta there
                break
            conn.sendall(data)  # send it to client