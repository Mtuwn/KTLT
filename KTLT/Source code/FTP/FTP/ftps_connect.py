import ftplib
#Thư viện này cung cấp các chức năng để tạo và tương tác với một kết nối FTP.

#tải về một tệp từ máy chủ FTP bằng cách sử dụng giao thức FTP
# và ghi nội dung của tệp đó vào một tệp cục bộ trên máy tính của người dùng.
def downl(ftp):
    ftp.dir()
    #Hàm này được sử dụng để liệt kê nội dung của thư mục hiện tại trên máy chủ FTP.
    # Điều này giúp người dùng biết các tệp có sẵn để tải về.
    temp_filename = input("Input file to download: ")
    # Hàm này yêu cầu người dùng nhập tên tệp mà họ muốn tải về từ máy chủ FTP.
    try:
        with open(temp_filename, 'wb') as temp_file:
        #Đoạn mã này mở một tệp cục bộ với tên temp_filename (tên mà người dùng đã nhập) ở chế độ ghi nhị phân ('wb').
        # Điều này cho phép chương trình ghi dữ liệu nhị phân vào tệp.
            ftp.retrbinary('RETR ' + temp_filename, temp_file.write)
        #Hàm này được sử dụng để tải về tệp từ máy chủ FTP và ghi nội dung vào tệp cục bộ mở ở bước trước.
        # Phương thức retrbinary() yêu cầu máy chủ FTP gửi dữ liệu nhị phân của tệp
        # được chỉ định bởi đối số 'RETR ' + temp_filename và ghi dữ liệu vào tệp cục bộ temp_file.write.
        print("[+] Download file: " + temp_filename)
        #tải về thành công thì in thông báo,tên tệp
    except:
        print("[+] Could not download file")
        #Nếu có bất kỳ lỗi nào xảy ra trong quá trình tải về
        # một thông báo lỗi sẽ được in ra để thông báo cho người dùng rằng không thể tải về tệp.


def upload(ftp):
    page = input("Input file to upload: ")
    #Hàm này yêu cầu người dùng nhập tên của tệp mà họ muốn tải lên lên máy chủ FTP.
    temp_filename = page
    #Tên tệp mà người dùng đã nhập được gán cho biến temp_filename.
    try:
        with open(temp_filename, 'rb') as temp_file:
            # Đoạn mã này mở tệp cục bộ với tên temp_filename ở chế độ đọc nhị phân ('rb').
            # Điều này cho phép chương trình đọc dữ liệu nhị phân từ tệp.
            ftp.storbinary(f"STOR {temp_filename}", temp_file)
            #Hàm này được sử dụng để tải lên tệp từ máy tính người dùng lên máy chủ FTP.
            # Phương thức storbinary() yêu cầu máy chủ FTP nhận dữ liệu nhị phân từ tệp cục bộ temp_file
            # và lưu nó dưới dạng tệp với tên được chỉ định bởi biến temp_filename.
    except Exception as e:
        print(e)
        #in ra thông báo lỗi


def dele(ftp):
    temp_filename = input("Input file to delete: ")
    # Hàm này yêu cầu người dùng nhập tên của tệp mà họ muốn xóa trên máy chủ FTP.
    try:
        ftp.delete(temp_filename)
        #Hàm này được sử dụng để gửi yêu cầu xóa tệp với tên được chỉ định (temp_filename) tới máy chủ FTP.
        # Nếu tệp tồn tại và người dùng có quyền truy cập để xóa nó, tệp sẽ được xóa từ máy chủ FTP.
        print("[+] Deleted successful") # hiển thị xóa thành công
    except:
        print(f"[+] Couldn't delete file {temp_filename}")
        # không thể xóa tệp với tên chỉ định là temp_filename


def main():
    host = "192.168.255.130" #địa chỉ ip mặc địch của FTP
    port = 21               # cổng mặc địch của FTP
    try:
        ftp = ftplib.FTP_TLS(timeout=30)
        #Tạo một đối tượng FTP_TLS từ thư viện ftplib.
        # Điều này sẽ khởi tạo một kết nối FTP bảo mật TLS.
        # Tham số timeout=30 đặt thời gian chờ kết nối là 30 giây.
        ftp.connect(host, port) # Kết nối đến máy chủ FTP với địa chỉ và cổng đã được chỉ định.
        ftp.auth() #Xác thực với máy chủ FTP
        print(f"Connected to {host}") #In ra thông báo cho người dùng rằng kết nối đã được thành công với máy chủ FTP.
        
    except:
        print("connection refused") # Nếu kết nối bị từ chối, một thông báo lỗi sẽ được in ra và chương trình sẽ kết thúc.
        return
    username = input("Username: ")
    pwd = input("Password: ")
    #Yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng nhập vào máy chủ FTP.
    try:
        ftp.login(username, pwd)
        # Đăng nhập vào máy chủ FTP với tên người dùng và mật khẩu đã nhập.
        ftp.prot_p() # Bảo vệ kết nối bằng cách sử dụng TLS.
        print("Login Successful") #In ra thông báo cho người dùng rằng đăng nhập đã thành công.
        print(ftp.pwd())
        ftp.dir() #Liệt kê nội dung của thư mục hiện tại trên máy chủ FTP.
    except Exception as e:
        print("Login Fail") # ngoại lệ in ra đăng nhập thất bại
        print(e)
    while True:
        print("\nMenu:")    #Người dùng chọn một tùy chọn từ menu.
        print("1. Upload")
        print("2. Download")
        print("3. Delete")
        print("4. Exit")
        choice = int(input("Chooice (1/2/3/4): "))

        if choice == 1:   #Nếu người dùng chọn tải lên (1), hàm upload(ftp) sẽ được gọi.
            upload(ftp)
            ftp.dir()
        elif choice == 2: #Nếu người dùng chọn tải về (2), hàm downl(ftp) sẽ được gọi.
            downl(ftp)
        elif choice == 3: #Nếu người dùng chọn xóa (3), hàm dele(ftp) sẽ được gọi.
            dele(ftp)
            ftp.dir()
        elif choice == 4: #Nếu người dùng chọn thoát (4), chương trình sẽ in ra thông báo và thoát khỏi vòng lặp.
            print("Exited")
            break
        else:  #Nếu người dùng chọn một lựa chọn không hợp lệ, thông báo lỗi sẽ được in ra.
            print("Invalid selection. Please select again...")

    ftp.quit() #Kết thúc kết nối FTP


if __name__ == "__main__":
    main()
    #Đảm bảo rằng chương trình sẽ chỉ chạy khi được gọi trực tiếp, không phải khi được nhập vào một chương trình khác.