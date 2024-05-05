import ftplib
#Thư viện này cung cấp các chức năng để tạo và tương tác với một kết nối FTP.
def read_file_from_ftp(ftp, filename):
    #hàm này nhận hai tham số:
    #ftp: Một đối tượng FTP từ thư viện ftplib, sử dụng để thực hiện các thao tác FTP.
    #filename: Tên của tệp tin trên máy chủ FTP mà bạn muốn đọc.
    file_content = bytearray() #Khởi tạo một đối tượng bytearray để lưu trữ nội dung của tệp tin.
    ftp.retrbinary('RETR ' + filename, file_content.extend)
    # Sử dụng phương thức retrbinary của đối tượng FTP để truy xuất tệp tin từ máy chủ FTP và đọc nội dung vào đối tượng bytearray.
    # Phương thức extend được sử dụng để mở rộng đối tượng bytearray với dữ liệu nhận được từ máy chủ.
    return file_content.decode('utf-8')
# Trả về nội dung của tệp tin dưới dạng chuỗi đã được giải mã từ bytearray sang UTF-8.


host = '192.168.255.130' #ip máy chủ
port = 21 #cổng
ftp_user = 'client1' #tk và mk người dùng
ftp_pass = 'client1'
filename = input("Path: ") # Yêu cầu người dùng nhập đường dẫn tệp tin trên máy chủ FTP.


try:
    ftp = ftplib.FTP_TLS(timeout = 30) # Tạo một đối tượng FTP_TLS từ thư viện ftplib, sử dụng giao thức FTP bảo mật.
    ftp.connect(host, port) #Kết nối đến máy chủ FTP thông qua địa chỉ host và cổng port.
    ftp.auth() #Xác thực với máy chủ FTP.
    print(f"Connected to {host}")
    ftp.login(ftp_user, ftp_pass) #Đăng nhập vào máy chủ FTP với tên người dùng và mật khẩu được cung cấp.
    ftp.prot_p() #Bảo vệ kết nối bằng cách sử dụng giao thức SSL/TLS.
    print("Login sucessful") #hiển thị đăng nhâp thành côgn
except:
        print("connection refused") #In ra thông báo lỗi cho biết kết nối bị từ chối nếu có lỗi xảy ra.
file_content = read_file_from_ftp(ftp, filename) #truyền tham số và chạy hàm
print(file_content)
