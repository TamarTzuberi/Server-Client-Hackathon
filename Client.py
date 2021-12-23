Client

from socket import *

host = "127.0.0.1"
port = 13117
server = ("127.0.0.2",13120)
msgFromClient = "Hello UDP Server"
bufferSize = 1024
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.bind((host,port))

message = input()
while message!='q':
    # Send to server using created UDP socket
    UDPClientSocket.sendto(message.encode('utf-8'), server)
    data, adress = UDPClientSocket.recvfrom(bufferSize)
    data = data.decode('utf-8')
    print(data)
    #message = input()
UDPClientSocket.close()

