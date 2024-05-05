import socket

serverPort = 12000
host = "127.0.0.1"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind(("", serverPort))
print("\t\tServer")
print("This server is ready to receive: ")
while 1:
    msg, clientAddress = serverSocket.recvfrom(2048)
    print(msg.decode())
    modifedMsg = msg.upper()
    serverSocket.sendto(modifedMsg, clientAddress) 

    