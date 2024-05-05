import ftplib 

def returnDefault(ftp, path): 
    ftp.cwd(path) 
    ftp.dir()
def main():
    host = "192.168.255.130"
    port = 21
    try:
        ftp = ftplib.FTP_TLS(timeout=30) 
        ftp.connect(host, port) 
        ftp.auth() 
        print(f"Connected to {host}")
    except:
        print("connection refused")
        return
    username = 'client1'
    passwd = 'client1'
    try:
        ftp.login(username, passwd) 
        ftp.prot_p()
        print('\nLogon succeeded')
        path = input("Enter the path to scan the file: ")
        returnDefault(ftp, path)
    except Exception as E:
        print(E)
if __name__ == "__main__":
    main()


