import ftplib
def renameFtpFilenames (ftpHost, ftpPort, ftpUser, ftpPass): 
    try: 
        ftp=ftplib.FTP_TLS(timeout = 30)
    # Kết nối đến ftp server 
        ftp.connect(ftpHost, ftpPort)
    # đăng nhập vào ftp server 
        ftp.auth()
        ftp.login(ftpUser, ftpPass)
    # sử dụng hàm prot p để xác thực dữ liệu 
        ftp.prot_p()
        ftp.dir()
    except Exception as e:
        print(e)


ftpHost='192.168.255.130'
ftpPort=21
ftpUser='client1'
ftpPass='client1'
# localFile = 'abc.txt'
fnames = renameFtpFilenames (ftpHost, ftpPort, ftpUser, ftpPass)
print("complete")