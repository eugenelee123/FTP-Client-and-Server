import socket
import sys

if(len(sys.argv) < 2):
    print("USAGE python", sys.argv[0], " < PORT NUMBER>")
    exit()
listenPort = int(sys.argv[1])
welcomeSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

welcomeSock.bind(('', listenPort))
welcomeSock.listen(1)
print("Now listening on ",listenPort)

def receiveMessage(socket,numBytes):
    buffer = ""
    tmpBuffer = ""

    while len(buffer) < numBytes:
        tmpBuffer = str(socket.recv(numBytes))


        if not tmpBuffer:
            break
        buffer += tmpBuffer
    
    return buffer

while(1):
    clientSocket, address = welcomeSock.accept()
    print("Accepted connection from client: ", address)

    message = clientSocket.recv(1024).decode()
    if(message == "get"):
        print("get")
    elif(message == "put"):
        print("put")
    elif(message = "ls"):
        print("ls")
    
    # print(clientSocket.recv(1024))
    # fileSizeBuffer = receiveMessage(clientSocket,10)
    # fileSize = int(fileSizeBuffer)
    # print("File Size: ",fileSize)
    