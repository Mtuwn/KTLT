# Dùng để lấy class Request từ Modun urllib.request
# Class Request được sử dụng để xây dựng và gửi yêu cầu HTTP đến 1 Url được chỉ định
# Điều này cho phép chương trình python thực hiện các yêu cầu cao hơn chẳng hạn như chỉ định tiêu đề hoặc các tham số khác để tương tác với máy chủ web
from urllib.request import Request

# biến url để lưu địa chỉ url 
url='http://python.org'
# Biến user_agent dùng để lưu loại thiết bị, hệ điều hành và trình duyệt đang được yêu cầu đến máy chủ
USER_AGENT = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36'

def chrome_user_agent():
    # Tạo một đối tượng để gửi request tới url
    request = Request(url)
    # Thêm header User-agent với giá trị đã được lưu trữ ở biến USER_AGENT
    request.add_header('User-agent',USER_AGENT)
    print("Request Headers")
    print("---------------")
    # Duyệt qua các header và lấy các tên header và giá trị tương ứng
    for header,value in request.header_items():
        print(header,":",value)

if __name__ == '__main__':
    chrome_user_agent()
