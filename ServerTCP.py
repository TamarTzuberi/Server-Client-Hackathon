ServerTCP

from _thread import *
import threading
import socket

lock_t = threading.Lock()
bufferSize = 1024
host = ""
def threaded(client1):
    while (True):
        data = client1.recv(bufferSize)
        if not data:
            lock_t.release()
            break
        #ans = calc(data) 
        #client1.send(ans)
    client1.close()

def main():
    port = 13120
    serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    serverSocket.bind((host,port))
    serverSocket.listen(2) # to check how much we need


