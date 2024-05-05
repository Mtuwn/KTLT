# Thư viện requests để gửi yêu cầu HTTP đến máy chủ và xử lý phản hồi
import requests
# Thư viện Os được sử dụng để tương tác vpứo hệ thống máy tính(Trong bài này để lấy giá trị của biến môi trường)
import os




# os.environ.get() hàm này để truy cập đến các biến môi trường
Shodan_api_key = 'EBeU0lGqtIO6yCxVFCWC4nUVbvovtjo5'         # SHODAN_API_KEY = os.environ['WEBtbSYW686PvIx4MVPHSITYeEBBqtEX']
# Địa chỉ ip mà bạn muốn truy vấn thông tin
ip = '1.1.1.1'
def ShodanInfo(ip):
    try: 
        # ip là địa chỉ muốn truy vấn thông tin
        # key là api key của bạn, cung cấo cho shodan api để được xác thực và truy vấn đến các dịch vụ của họ
        #minify = true để chỉ định rằng các phản hồi shodan api nên được giảm kích thước của dữ liệu trả về (trả phí mới dùng được)
        # result = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={Shodan_api_key}&minify=True").json()
        result = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={Shodan_api_key}").json()
        
    except Exception as e: # Xuất thông báo lỗi nếu gặp lỗi
        result = {"Error":"Information not available"}
    return result

print(ShodanInfo(ip))