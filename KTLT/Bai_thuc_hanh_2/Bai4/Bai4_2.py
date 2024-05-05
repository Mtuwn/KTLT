# Modun nmap cung cấp giao diện tương tác với công cụ quét mạng nmap thông qua mã Python
# Nmap là công cụ mạng phổ biến được sử dụng để phân tích mạng và kiểm tra bảo mật mạng
# Modun nmap cho phép bạn sử dụng các tính năng của nmao từ trong chương trình python mà không cần thoát khỏi môi trường python
import nmap
# Tạo lớp NmapScanner gồm 2 phương thức là phương thức khởi tạo __init()__ và nmapScan
class NmapScanner:
    # Phương thức khởi tạo này được gọi mỗi khi đối tượng của lớp được tạo ra
    # Trong phương thức này, khởi tạo 1 đối tượng portScanner được tạo ra từ lớp PortScanner trong thư viện nmap
    def __init__(self):
        self.portScanner = nmap.PortScanner()
    # Phương thức này thực hiện quét các địa chỉ ip và cổng được chỉ định
    def nmapScan(self,ip_address, port):
        # Nó sử dụng hàm scan() của đối tượng portScanner để thực hiện quét và lưu trữ kết quả trong đối tượng portScanner
        self.portScanner.scan(ip_address,port)
        # In ra các dòng lệnh mà bạn đã sử dụng bao gồm cả tên chương trình và đối số truyền vào
        print("[+] Executing command: ",self.portScanner.command_line())

# Hàm main là hàm bắt đầu khi chương trình được thực thi
def main():
    # Nhập địa chỉ ip muốn quét
    ip_address = input("Ip scan: ")
    # Danh sách các cổng mạng muốn quét
    # port 21: sử dụng cho dịch vụ ftp
    # port 22: ssh
    # port 23: telnet
    # port 25: smtp
    # port 80: http
    # port 443: hhtps
    ports = ["21","22","23","25","80","443"]
    # Với mỗi cổng trong danh sách ports, nó sẽ khởi tạo đối tượng mới của lớp NmapScanner
    # Gọi đến phương thức nmapScan của đối tượng NmapScanner
    # Sau đó nmapScan(ip_address,port) sẽ thực hiện quét các cổng trên địa chỉ IP đã được nhập
    for port in ports:
        NmapScanner().nmapScan(ip_address, port)


if __name__ == "__main__":
    main()