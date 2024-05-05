# Mô-đen socket tạo thành cơ sở cỉa tất cả các giao tiếp mạng trong python
# Bằng cách bao gồm dòng này, sẽ có thể tạo thành các socket trong chương trình
import socket

# Khai báo tên server và port
serverName = '127.0.0.1'
serverPort = 12000
# Tạo biến format để mã hóa và giải mã trong quá trình giao tiếp giữa client và server
Format = 'utf8'

# Tạo socket của client, clientSocket
# - Tham số đầu tiên cho biết kiểu địa chỉ ip, cụ thể là À_INET chỉ ra mạng đang sử dụng là IPv4
# - Tham số thứ 2 cho biết loại socket là TCP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sử dụng khối lệnh try - except để xử lý các ngoại lệ trong quá trình giao tiếp của server và client
try:
    # Hàm connect cho phép kết nối với máy chủ có địa chỉ là serverName và cổng là serverPort
    clientSocket.connect((serverName,serverPort))
    # Xuất ra địa chỉ và port của client
    print("client address: ",clientSocket.getsockname())
    # Khởi tạo biến msg lưu trữ thông điệp giao tiếp của client và server
    msg = ""
    
    # Vòng lặp này sẽ xử lý các thông điệp giao tiếp của client và server cho đến khi người dùng  nhập thông điệp mdg là end thì dừng
    while msg != "END":
        # Hàm input dùng để nhận dữ liệu đầu vào từ bàn phím
        msg = input('input lowercase sentence: ')
        # Hàm sendall đảm bảo rằng toàn bộ dữ liệu được gửi và được mã hóa bằng hàm encode
        clientSocket.sendall(msg.encode(Format))
         #hàm recv dùng để nhận dữ liệu từ client
        # 1024 là số byte tối đa nhận được là 1024
        # hàm decode(Format) là để giải mã thông điệp của client chuyển thông điệp thành chuỗi sử dụng utf-8
        msg = clientSocket.recv(1024).decode(Format)
        # Xuất ra thông điệp nhận được từ phía server
        print("Sever said: ",msg)
        
except:
    print("ERROR")

# Đóng kết nối    
clientSocket.close()