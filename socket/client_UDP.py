import socket 

serverPort = 12000
host = '127.0.0.1'

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input('input lowercase sentence: ')
clientSocket.sendto(msg.encode(),(host,serverPort))
modifiedMsg, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMsg.decode())

clientSocket.close()



