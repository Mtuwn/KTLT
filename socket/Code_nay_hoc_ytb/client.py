import socket
import tkinter as tk

HOST = "127.0.0.1"
SERVER_PORT = 65412
FORMAT = "utf8"
Login = "login"


Login = "login"
Fail = "fail"
Ok = "ok"
End = "x"

class StartPage(tk.Frame):
    def __init__(self, parent, appController):
        tk.Frame.__init__(self, parent)
        
        label_title = tk.Label(self, text="Login")
        label_user = tk.Label(self, text="username ")
        label_pwd = tk.Label(self, text="password ")
        self.label_notice = tk.Label(self, text="",bg="bisque2")
        self.entry_user = tk.Entry(self, width=20, bg="light yellow")
        self.entry_pwd = tk.Entry(self, width=20, bg="light yellow")
        btn_login = tk.Button(self, text="LOG IN", width=10, command=lambda: appController.login(self, client))
        
        label_title.pack()
        label_user.pack()
        self.entry_user.pack()
        label_pwd.pack()
        self.entry_pwd.pack()
        self.label_notice.pack()
        
        btn_login.pack()

class HomePage(tk.Frame):
    def __init__(self, parent, appController):
        tk.Frame.__init__(self,parent) ## subclass

        label_title = tk.Label(self, text="Home Page")
        btn_logout = tk.Button(self, text="Log out", command=lambda: appController.showPage(StartPage))
        
        label_title.pack()
        btn_logout.pack()

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title("My App")
        self.geometry("500x200")
        self.resizable(width=False, height=False)
        
        container = tk.Frame()
        
        container.config(bg="red")
        container.pack()
        
        self.frames = {}
        
        for F in (StartPage, HomePage):
            frame = F(container, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[F] = frame
        
        self.frames[StartPage].tkraise()
        
    def showPage(self, FrameClass):
        self.frames[FrameClass].tkraise()

    def login(self, curFrame, sck: socket):
        
        try: 
            user = curFrame.entry_user.get()
            pwd = curFrame.entry_pwd.get()
            
            if(user == "" or pwd == ""):
                curFrame.label_notice["text"] = "Fields cannot be empty"
                return

            
            option = Login
            sck.sendall(option.encode(FORMAT))

            sck.sendall(user.encode(FORMAT))
            sck.recv(1024)
            sck.sendall(pwd.encode(FORMAT))
            sck.recv(1024)
            
            # recv respone log in check
            msg = sck.recv(1024).decode(FORMAT)
            
            if(msg == Fail):
                curFrame.label_notice["text"] = "Invalid user or password"
                return
            else:
                self.showPage(HomePage)
                            
            
        except:
            print("Error: Server is not response")   
        
#---------------main--------------------
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,SERVER_PORT))

app = App()
app.mainloop()





# def sendlist(client:socket,list):
    
#     for item in list:
#         client.sendall(item.encode(FORMAT))
#         client.recv(1024)
        
#     msg = "end"
#     client.sendall(msg.encode(FORMAT))

# def clientLogin(client):
#     account = []
#     username = input("username: ")
#     password = input("password: ")
#     account.append(username)
#     account.append(password)
#     #send account to server
#     sendlist(client, account)
    
#     #receive respone from server
#     validCheck = client.recv(1024).decode(FORMAT)
#     print(validCheck)
    
    
        
# print("Client side")

# client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# try: 
#     client.connect((HOST,SERVER_PORT))
#     print("client address: ",client.getsockname())
    
#     list = ["Trần Minh Tuấn","20", "Nam"]

#     msg = None
#     while(msg != "x"):
#         msg = input("talk: ")
#         client.sendall(msg.encode(FORMAT)) 
#         if(msg == Login):
#             msg = client.recv(2024).decode(FORMAT)
#             clientLogin(client)
# except: 
#     print("Error")
    
# input()
# client.close()