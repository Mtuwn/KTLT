import socket

ip =  '42.113.206.24'  #ip danchi.com.vn
portlist = [21,22,23,80,443]
for port in portlist:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((ip,port))
    print(port, ':', result)
    sock.close()