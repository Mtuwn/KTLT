# Modun nmap cung cấp giao diện tương tác với công cụ quét mạng nmap thông qua mã Python
# Nmap là công cụ mạng phổ biến được sử dụng để phân tích mạng và kiểm tra bảo mật mạng
# Modun nmap cho phép bạn sử dụng các tính năng của nmao từ trong chương trình python mà không cần thoát khỏi môi trường python
import nmap

# Tạo một đối tượng PortScannerAsync để quét cổng không đồng bộ
nma = nmap.PortScannerAsync()
# Đây là hàm callback sẽ được gọi khi có kết quả quét trả về
def callback_result(host, scan_result):
    print ('------------------')
    print (host, scan_result)
if __name__ == "__main__":
    ports = ["21","22","23","24","80"]
# Chúng ta quét từng cổng trong danh sách ports bằng cách sử dụng phương thức scan của PortScannerAsync.
#  Đối số arguments chỉ định các đối số cho quá trình quét, ở đây là cổng muốn quét
# Hàm callback sẽ được gọi khi có kết quả quét trả về
    for port in ports:
        nma.scan('scanme.nmap.org', arguments=f"-p {port}", callback=callback_result)
   
    # still_scanning() kiểm tra quá trình quét xem còn xảy ra hay không
    while nma.still_scanning():
        print("Waiting >>>")
        # nma.wait(None) để đợi quá trình quét kết thúc.
        nma.wait(None)  
        