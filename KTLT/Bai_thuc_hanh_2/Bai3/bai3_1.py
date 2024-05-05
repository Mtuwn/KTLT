# Một thư viện phổ biến dùng để giúp lập trình viên có thể thực hiện cac tác vụ như gửi request tới server
# Cũng như xử lý response một cách đơn giản
import requests

# Khởi tạo danh sách logins để lưu trữ các predictable URL
logins = [] 
# Mở tệp Logins.txt để đọc dùng with để tự động đóng file khi hoàn thành công việc
with open('Logins.txt', 'r') as f:
    # Duyệt qua từng dòng trong tệp Logins.txt
    for line in f:
        line = line.strip() #loại bỏ khoảng trắng và kí tự xuống dòng từ dòng đang xem xét và gán nó cho biến line
        # Thêm các predictable URL vào danh sách logins bằng hàm append()
        logins.append(line)
# Domain mục tiêu, nơi sẽ được gửi để kiểm tra sự tồn tại của tài nguyên
domain = "http://testphp.vulnweb.com"
# Duyệt qua từng predictable URL trong danh sách logins
for login in logins:
    print("Check... " +  domain + login)
    # Gửi yêu cầu đến địa chỉ url được tạo ra từ domain và predictable URL
    response = requests.get(domain+login)
    # nghĩa là trang login đã được tìm thấy trong máy chủ
    if response.status_code == 200:
        print("Login resource detected:"+login)