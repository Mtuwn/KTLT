import ftplib #Thư viện này cung cấp các chức năng để tạo và tương tác với một kết nối FTP.
def anonLogin(hostname, port): # Hàm này xác thực xem FTP Server có cho phép đăng nhập với tư các người dùng ẩn danh không
    try:
        ftp = ftplib.FTP_TLS(timeout = 30)
        #Tạo một đối tượng FTP_TLS từ thư viện ftplib để thực hiện kết nối FTP bảo mật.
        #timeout = 30 đặt timeout cho kết nối là 30 giây.
        ftp.connect(host, port) #Kết nối đến máy chủ FTP thông qua địa chỉ host và cổng port.
        ftp.auth() #xác thực với máy chủ FTP
        print(f"Connected to {host}")
    except: 
        print("connection refused") 
        return  #Nếu có lỗi thì dừng
    try:

        ftp.login('anonymous') #Thực hiện đăng nhập vào máy chủ FTP với tên người dùng 'anonymous'.
        print('\n[*]' + str(hostname) +'FTP Anonymous Logon Succeeded')
        ftp.quit() #đóng kết nối FTP
        return True #trả về true để chỉ ra rằng đăng nhập ẩn danh thành công
    except Exception:
        print('\n[-]' + str(hostname) + ' FTP Anonymous Logon Failed')
        return False

host = "192.168.255.130" #ip máy chủ FTP
port = 21 #port máy chủ
anonLogin(host,port)