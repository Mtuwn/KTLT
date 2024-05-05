import socket
import threading
import pyodbc

HOST = "127.0.0.1"
SERVER_PORT = 65412
FORMAT = "utf8"

Login = "login"
Fail = "fail"
Ok = "ok"
End = "x"

def recvList(conn):
    list = []
    item = conn.recv(1024).decode(FORMAT)

    while (item != "end"):
        list.append(item)
        conn.sendall(item.encode(FORMAT))
        item = conn.recv(1024).decode(FORMAT)

    return list

def handleClient(conn: socket, addr):
    print("conn: ",conn.getsockname())

    option = conn.recv(1024).decode(FORMAT)

    count = 0
    while(count < 50):
        if(option == Login):
            serverLogin(conn)
            option = "x"
        count += 1
    
    print("Client ", addr, "finally, close")
    print(conn.getsockname(), " close")
    conn.close()
    
def serverLogin(conn:socket):
    print("Login start")

    user = conn.recv(1024).decode(FORMAT)
    conn.sendall(user.encode(FORMAT))
    pwd = conn.recv(1024).decode(FORMAT)
    conn.sendall(pwd.encode(FORMAT))
    
    cusor.execute("select pass from Account where username = ?", user)

    password = cusor.fetchone()
    data_password = password[0]
    
    msg = Ok
    
    if(pwd == data_password):
        msg = Ok
    else: 
        msg = Fail

    
    conn.sendall(msg.encode(FORMAT))
    
    
    
# ---------------main-------------------------    
 
conx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=LAPTOP-S1L4C1MF; DATABASE=Socket_Account; UID=sa; PWD=16040312b;')
# creates a cursor object for the established database connection
cusor = conx.cursor()

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((HOST,SERVER_PORT))
server.listen()
print("SERVER SIDE")
print("server: ",HOST,SERVER_PORT)
print("waiting for client")

nClient = 0

while(nClient <3):
    
    try: 
        conn, addr = server.accept()
        thr = threading.Thread(target=handleClient, args=(conn, addr))
        thr.daemon = False
        thr.start()
        
    except:
        print("Error")
        
    nClient += 1
    

server.close()