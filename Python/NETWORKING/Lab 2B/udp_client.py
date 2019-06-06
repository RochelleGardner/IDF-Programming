import socket
import json

msgFromClient = "Hello UDP Server"
dictFromClient = {
    'name':'Rochelle',
    'class':'IDF',
    'date':'today',
}
dicFromC = json.dumps(dictFromClient)
bytesToSend = str.encode(msgFromClient)
secondBTS = str.encode(dicFromC)
serverAddressPort = ("127.0.0.1", 20001)

# Create a UDP socket at client side
#UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # Send to server using created UDP socket
    #UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    s.sendto(bytesToSend, serverAddressPort)
    s.sendto(secondBTS, serverAddressPort)

    #msgFromServer = UDPClientSocket.recvfrom(1024)
    #msg = "Message from Server {}".format(msgFromServer[0])
    msgFromServ = s.recvfrom(1024)
    msg = "Message from Server: {}".format(msgFromServ[0])

