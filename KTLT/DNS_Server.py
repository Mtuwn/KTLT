# dns.resolver là một phần của gối dnspython
# Cho pép thực hiện các truy vấn DNS như lấy địa chỉ ip
# Tìm kiếm bản ghi MX(Mail exchange)
# Bản ghi NS(Name server) và nhiều truy vấn khác
import dns.resolver

hosts = ['oreilly.com','yahoo.com','google.com','microsoft.com','cnn.com','testphp.vulnweb.com']
for host in hosts:
    print(host)
    # dns.resolver.query được thực hiện truy vấn DNS kiểu A với một tên miền cụ thể
    # A : ipv4
    # AAA : ipv6
    # CNAME(canonical Name): lấy tên miền chính thức của một tên miền alias(nick name)
    # NS: Name Server
    # TXT: Truy vấn để lấy các bản ghi TXT, thường được sử dụng để lưu trữ các thông tin mô tả cho tên miền.
    # SOA: Xác định thông tin máy chủ tên miền chịu trách nhiện về thông tin cơ bản về tên miền
    # PTR: truy vấn để lấy tên miền chính thức của địa chỉ ip
    ip = dns.resolver.query(host,'A')
    # dns.resolver.resolve(name, retype): Tương tự query nma trả về danh sach các đối tượng dns.resolver.Answer thay vì trình tự đối tượng
    #dns.resolver.NXDOMAIN: Một lớp ngoại lệ được sử dụng khi truy vấn DNS không tồn tại.
    #dns.resolver.NoAnswer: Một lớp ngoại lệ được sử dụng khi truy vấn DNS không có kết quả
    # dns.resolver.Timeout: Một lớp ngoại lệ được sử dụng khi truy vấn DNS vượt quá thời gian chờ.
    # dns.resolver.NoNameservers: Một lớp ngoại lệ được sử dụng khi không có máy chủ tên miền được cấu hình.
    # dns.resolver.get_default_resolver(): Trả về trình giải quyết mặc định cho hệ thống.
    for i in ip:
        print(i)