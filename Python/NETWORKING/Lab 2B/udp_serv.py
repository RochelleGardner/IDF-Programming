import socket
import json

HOST = "127.0.0.1"
PORT = 20001

msgFromServer       = "Message Received!"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
#UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # Bind to address and ip    
    #UDPServerSocket.bind((localIP, localPort))    
    s.bind((HOST, PORT))
    #print("UDP server up and listening")
    print("UDP server listening")

    # Listen for incoming datagrams
    #while(True):
    while True:
        #bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        data = s.recvfrom(1024)
        #message = bytesAddressPair[0]
        message = data[0]
        message.decode()
        #address = bytesAddressPair[1]
        address = data[1]

        # print dictionary from client
        #msg = json.loads(message)[0]
        print ("Message from Client at ", address, " : ", message)
        #clientMsg = "Message from Client:{}".format(message)
        #clientIP  = "Client IP Address:{}".format(address)

        # Sending a reply to client
        # #UDPServerSocket.sendto(bytesToSend, address)
        s.sendto(bytesToSend, address)
        