import socket
import sys
import os

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

def get(message, clientSocket, machine):
    message = message.split(" ",1)
    fileName = message[1]
    fileObj = open(fileName, "r")

    fileData = fileObj.read(65536)

    clientSocket.sendto(fileData.encode(),(machine,listenPort))

    fileObj.close()

def put():
    return
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
machine = clientSocket.recv(1024).decode()

while(1):
    message = clientSocket.recv(1024).decode()
    if("get" in message):
        get(message, clientSocket, machine)
        print("Sent file info")
    elif("put" in message):
        print("put")
    elif(message == "ls"):
        ls(clientSocket)
        print("Sent directory info")

    # print(clientSocket.recv(1024))
    # fileSizeBuffer = receiveMessage(clientSocket,10)
    # fileSize = int(fileSizeBuffer)
    # print("File Size: ",fileSize)
