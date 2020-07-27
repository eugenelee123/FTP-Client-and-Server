import socket
import sys

if(len(sys.argv) < 2):
    print("USAGE python", sys.argv[0], " < PORT NUMBER>")
    exit()
listenPort = int(sys.argv[1])
welcomeSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

welcomeSock.bind(('', listenPort))
print("Socked binded to ", listenPort)
welcomeSock.listen(1)
print("Now listening on ",listenPort)

while(1):
    connection, address = welcomeSock.accept()
    print("Connected to ", address)
