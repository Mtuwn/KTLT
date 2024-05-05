#Mô-đun socket tạo thành cơ sở của tất cả các giao tiếp mạng trong python
#Bằng cách bao gồm dòng này, sẽ có thể tạo các socket trong chương trình
import socket

# Khai báo tên server và port
serverName = '127.0.0.1'
serverPort = 12000
# Tạo biến format để mã hóa và giải mã trong quá trình giao tiếp giữa client và server
Format = 'utf8'

# Tạo socket của server
# - Tham số đầu tiên cho biết kiểu địa chỉ ip, cụ thể là AF_NET chỉ ra mạng đang được sử dụng là IPv4
# - Tham số thứ 2 cho biết loại socket là TCP
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# bind cho phép nó nhận các kết nối đến địa chỉ serverName và cổng serverPort
server.bind((serverName, serverPort))
# Hàm listen để khởi động các máy chủ lắng nghe đến các kết nối đến
server.listen()

# Xuất ra màn hình 
print("SERVER SIDE")
print("server: ",serverName,serverPort)
print("waiting for client")

# Sử dụng khối lệnh try - except để xử lý các ngoại lệ trong quá trình giao tiếp của server và client
try:
    #Server chấp chập một kết nối đến thông qua hàm accept
    #Đồng thời tạo một đối tượng socket mới để lưu giá trị trả về là conn để giao tiếp với client và addr là địa chỉ của client
    conn,addr = server.accept()
    # Xuất ra màn hình địa chỉ của client cũng như thông báo việc server sẵn sàng nhận dữ liệu
    print("cilent address: ",addr)
    print("This server is ready to receive: ")
    # Khơi tạo biến msg để lưu trữ thông điệp từ phía client
    
    msg = ""
    # Vòng lặp này sẽ xử lý các thông điệp giao tiếp của client và server cho đến khi server nhận được thông điệp end thì dừng
    while msg != 'END':
        #hàm recv dùng để nhận dữ liệu từ client
        # 1024 là số byte tối đa nhận được là 1024
        # hàm decode(Format) là để giải mã thông điệp của client chuyển thông điệp thành chuỗi sử dụng utf-8
        msg = conn.recv(1024).decode(Format)
        # Xuất thông điệp ra màn hình
        print(msg)
        # Hàm upper chuyển thông điệp thành chữ in hoa
        msg = msg.upper()
        # Hàm sendall đảm bảo rằng toàn bộ dữ liệu được gửi và được mã hóa bằng hàm encode
        conn.sendall(msg.encode(Format))
        
except:
    print("ERROR")
    
# Đóng kết nối với client    
conn.close()

