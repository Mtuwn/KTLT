import ftplib #Thư viện này cung cấp các chức năng để tạo và tương tác với một kết nối FTP.


def returnDefault(ftp, path): # Hàm returnDefault có chức năng quét các file và thư mục có trong path
    ftp.cwd(path) #Thay đổi thư mục làm việc của FTP tới thư mục được chỉ định bởi biến path.
    ftp.dir() #Liệt kê các tệp và thư mục trong thư mục hiện tại của FTP.
def main():
    host = "192.168.255.130"
    port = 21 # Khai báo biến host và port để chứa địa chỉ và cổng của máy chủ FTP.
    try:
        ftp = ftplib.FTP_TLS(timeout=30) #Tạo một đối tượng FTP_TLS từ thư viện ftplib, sử dụng giao thức FTP bảo mật TLS.
        ftp.connect(host, port) #Kết nối đến máy chủ FTP sử dụng địa chỉ và cổng được cung cấp.
        ftp.auth() #xác thực với máy chủ FTP
        print(f"Connected to {host}")
    except:
        print("connection refused")
    username = 'client1'
    passwd = 'client1'
    try:
        ftp.login(username, passwd) #Đăng nhập vào máy chủ FTP với tên người dùng và mật khẩu được cung cấp.
        ftp.prot_p() #Bảo vệ kết nối bằng cách sử dụng giao thức SSL/TLS.
        print('\nLogon succeeded')
        path = input("Enter the path to scan the file: ")
        returnDefault(ftp, path)
    except Exception as E:
        print(E)
if __name__ == "__main__":
    main()


