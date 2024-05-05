import nmap

# Khởi tạo đối tượng portscanner
portScanner = nmap.PortScanner()
# Xác định địa chỉ ip muốn quét 
hostScan = input("Host Scan: ")
# quét các cổng 21 (FTP), 23 (Telnet), 80 (HTTP), và 3389 (Remote Desktop Protocol)
portList = "20,21,22,23,80,3389"
# -n: Không thực hiện giải quyết tên miền. Điều này có thể giúp tăng tốc độ quét bằng cách tránh giải quyết địa chỉ IP thành tên miền.
#-p: port
#-sS: quét tcp gửi gói syn
#-sU: quét UDP
#-O: xác định hệ điều hành máy chủ
#-sP: Quét để xác định các host hoạt động
# -PA21,23,80,3389: Gửi gói tin TCP ACK đến các cổng 21 (FTP), 23 (Telnet), 80 (HTTP), và 3389 (Remote Desktop Protocol)
portScanner.scan(hosts=hostScan,arguments=f"-n -p{portList}")
# In ra các dòng lệnh mà bạn đã sử dụng bao gồm cả tên chương trình và đối số truyền vào
print(portScanner.command_line())
# Tạo ra danh sách gồm host và trang thái và lưu nó vào host_list
#portScanner.all_hosts trả về danh sách máy chủ đã được quét bởi portScanner
# portScanner[x]['status']['state'] gồm: 
## portScanner[x] truy cập thông tin của máy chủ có địa chỉ ip là x
## portScanner[x]['status'] truy cập đến thông tin của máy chủ có địa chỉ ip là x dữ liệu trả về là dir vd: {'state': 'up', 'reason': '', 'reason_ttl': 0}
## portScanner[x]['status']['state']: Truy cập trực tiếp vào trạng thái 
# for x in portScanner.all_hosts() để duyệt qua từng máy chủ trong danh sách trên.Biến x sẽ lần lượt chứa địa chỉ ip của các máy chủ
# (x, portScanner[x]['status']['state']): Đồng thời trong mỗi vòng lặp, tạo các cặp gồm địa chỉ ip x và trạng thái của máy chủ
host_list = [(x,portScanner[x]['status']['state']) for x in portScanner.all_hosts()]
# Duyệt qua từng máy chủ trong host_list và trạng thái của nó
for host,status in host_list:
    # Xuất ra các máy chủ và trạng thái
    print(host,status)
    # portScanner[host].all_protocols() lấy ra các giao thức có sẵn của máy chủ
    for proto in portScanner[host].all_protocols():
        # Xuất ra các giao thức có sẵn trong máy chủ
        print("protocal",proto)
        # portScanner[host][proto] trả về kết quả là 1 dictionary nên keys() sẽ lấy giá trị key trong từng phần tử của dictionary. vd: {21: {'state': 'closed', 'reason': 'syn-ack', 'name': 'ftp'}} thì keys() trả về 21
        listport = portScanner[host][proto].keys()
        # In ra thông tin về cổng mạng đang mở bao gồm số cổng và trạng thái của cổng mạng
        for port in listport:
            print("port:",port,"State:",portScanner[host][proto][port]['state'])
