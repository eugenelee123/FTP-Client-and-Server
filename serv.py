import socket
import sys
import os
from functools import partial

if(len(sys.argv) < 2):
    print("USAGE python", sys.argv[0], " < PORT NUMBER>")
    exit()
DELIMITER = "%>%"
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

def get(message, clientSocket):
    message = message.split(" ",1)
    fileName = message[1]    
    fileObj = open(fileName, "rb")
    
    # Get file size
    counter = 0
    for chunk in iter(partial(fileObj.read, 64), b''):
        counter += 1

    # Send file size to the client
    clientSocket.send(str(counter).encode())
    fileObj.close()

    # Get a go ahead to continue
    clientSocket.recv(1024).decode()

    # Send the file to the client in chunks
    fileObj = open(fileName, "rb")
    for chunk in iter(partial(fileObj.read, 64), b''):
        clientSocket.send(chunk)
    fileObj.close()

def put(socket):
    # Let the client continue
    socket.send('go ahead'.encode())

    # Receive file size
    counter = socket.recv(64).decode()

    # Let the client continue
    socket.send('go ahead'.encode())

    # Receive and display file info looping by file size given by client
    print("Message received:")
    print(counter, " chunks")
    for i in range(int(counter)):
        print(socket.recv(64))

def ls(socket):

    directoryContents = os.listdir(os.getcwd())
    directorySize = len(directoryContents)
    directorySize = str(directorySize) + "\n"

    #Send directory size
    socket.send(directorySize.encode())

    for sendFile in directoryContents:
        # fileSize = sys.getsizeof(sendFile)
        # fileSize = str(fileSize) + DELIMITER
        # socket.send(fileSize.encode())
        sendFile += DELIMITER
        socket.send(sendFile.encode())


clientSocket, address = welcomeSock.accept()
print("Accepted connection from client: ", address)
while(1):

    message = clientSocket.recv(1024).decode()
    if("get" in message):
        get(message, clientSocket)
        print("Sent file info")
    elif("put" in message):
        put(clientSocket)
    elif(message == "ls"):
        ls(clientSocket)
        print("Sent directory info")
