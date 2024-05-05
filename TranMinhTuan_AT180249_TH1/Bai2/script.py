# Mô-đen socket tạo thành cơ sở cỉa tất cả các giao tiếp mạng trong python
# Bằng cách bao gồm dòng này, sẽ có thể tạo thành các socket trong chương trình
import socket

def check_open_services(server_ip):
    # Tạo 1 danh sách open_services rỗng để lưu trữ các port đang mở
    open_services = []
    # Kiểm tra các port từ 1 đến 1025
    for port in [21,22,23,80,443]:
        # Tạo socket của client, clientSocket
        # - Tham số đầu tiên cho biết kiểu địa chỉ ip, cụ thể là À_INET chỉ ra mạng đang sử dụng là IPv4
        # - Tham số thứ 2 cho biết loại socket là TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Thiết lập timeout là 1 giây
        sock.settimeout(1)
        # Thử kết nối tới các port của server_ip nếu kết nối thành công hàm connect_ex trả về 0 
        # Nếu không thành công sẽ trả về một giá trị khác 0
        conn = sock.connect_ex((server_ip,port))
        # Nếu kết nối thành công thêm port vào danh sách open_services
        if conn == 0 :
            open_services.append(port)
    # Đóng kết nối
    sock.close()
    # Trả về danh sách các port đang được mở trên server_ip
    return open_services

# Nhập địa chỉ ip muốn quét
server_ip = input("Input your server ip: ")

# Gọi đến hàm check_open_services để kiểm tra các cổng đang được mở trên server_ip
open_ports = check_open_services(server_ip)

# Nếu danh sách không rỗng
if open_ports:
    # Xuất dữ liệu
    # Hàm join giúp nối các phần tử trong open_ports thành một chuỗi được phân tách bởi dấu phẩy
    # Map giúp ánh xạ đến các phần tử của open_ports và chuyển đổi các phần tử thành dữ liệu string
    print("Open services on", server_ip,':', ', '.join(map(str,open_ports)))
    
# Ngược lại xuất ra không tìm thấy cổng nào
else:
    print("No open services found on the server.")