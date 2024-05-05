import socket

try: 
    print("gethostname: ", socket.gethostname())
    print("gethostbyname: ", socket.gethostbyname('www.actvn.edu.vn'))
    print("gethostbyname_ex: ", socket.gethostbyname_ex('www.actvn.edu.vn'))
    print("gethostbyaddr: ", socket.gethostbyaddr('8.8.8.8')) # dns của google
    print("getfqdn: ", socket.getfqdn('www.actvn.edu.vn'))
    print("getaddrinfo: ", socket.getaddrinfo("www.actvn.edu.vn",None,0, socket.SOCK_STREAM))
except socket.error as e:
    print(str(e))