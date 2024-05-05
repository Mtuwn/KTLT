import ftplib
def read_file_from_ftp(ftp, filename):
    ftp.retrbinary('RETR ' + filename, file_content.extend)
    return file_content.decode('utf-8')

host = '192.168.255.130'
port = 21 
ftp_user = 'client1'
ftp_pass = 'client1'
filename = input("Path: ") 


try:
    ftp = ftplib.FTP_TLS(timeout = 30) 
    ftp.connect(host, port)
    print(f"Connected to {host}")
    ftp.login(ftp_user, ftp_pass) 
    ftp.prot_p() 
    print("Login sucessful") 
except:
        print("connection refused") 
file_content = read_file_from_ftp(ftp, filename) 
print(file_content)
