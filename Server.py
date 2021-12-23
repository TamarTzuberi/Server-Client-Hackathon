Server

import socket
from threading import Thread
import time
import struct
from threading import Thread

class Server:

    def __init__(self,port):
        self.port = port
        self.host = socket.gethostname()
        self.state = False # False - not in game mode
        self.clients = []
        self.udp_thread = Thread(self.listeninigOnUDP())
        self.tcp_thread = Thread(self.listeningOnTCP())

    def listeninigOnUDP(self):
        while not self.state:
            server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            print("Server started, listening on IP address" , self.host)
            # Enable broadcasting mode
            server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            server.bind(self.host, self.port)
            # Set a timeout so the socket does not block
            # indefinitely when trying to receive data.
            server.settimeout(0.2)
            message = "offer to connect"
            while True:
                server.sendto(struct.pack(message), ('<broadcast>', 13117))
                #print("message sent!")
                time.sleep(1)

    def listeningOnTCP(self):
        connectionSucceess = False
        try:
            serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
            serverSocket.bind((self.host,self.port))
            serverSocket.listen(2)
            connectionSucceess = True
            self.tcp_thread.start()
            while 1:
                connectionSocket,addr = serverSocket.accept()
                clientName = connectionSocket.recv(1024)
                self.clients.append((clientName,addr,connectionSocket))
            
            self.state = True

        except:
            connectionSucceess = False
            

    def clientsStartGame(self):
        for client in self.clients:
            client[2].sendto("Game start.....",client[1])
            






