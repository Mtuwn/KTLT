import nmap

# in ra các phương thức và thuộc tính trong nmap
print(dir(nmap))
# Khởi tạo đối tượng của lớp PortScanner

scanner = nmap.PortScanner()
# Kiểm tra các thuộc tính có sẵn trong PortScanner
print(dir(scanner))