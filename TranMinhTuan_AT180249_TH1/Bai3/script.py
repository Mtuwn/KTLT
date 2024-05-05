# Một thư viện phổ biến dùng để giúp lập trình viên có thể thực hiện cac tác vụ như gửi request tới server
# Cũng như xử lý response một cách đơn giản
import requests

# Biến url chứa địa chỉ url mà ta muốm gửi yêu cầu đến
url='http://python.org'
# Biến User_agent lưu trữ giá trị của header user_agent
USER_AGENT = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36'


def chrome_user_agent():
    # Dòng này gửi 1 request get tới url chỉ định
    # Trong quá trình yêu cầu ta chỉ định thêm header user-agent cho request này
    # Điều này giúp mô phỏng việc truy cập từ một trình duyệt trên 1 thiết bị android
    # r là respone của request được gửi bằng thư viện requests
    r = requests.get(url, headers={'User-agent':f'{USER_AGENT}'})
    # Xuất ra giá trị của header user-agent trong request mà chúng ta gửi đi
    # r.requests.headers cho phép truy cập thông tin về request gồm các header. Dữ liệu trả về là 1 dictionary
    hearders = r.request.headers
    # Hàm items() được sử dụng để trả về một danh sách các cặp (hoặc tuple) khóa-giá trị từ một từ điển (dictionary). Mỗi cặp này bao gồm một khóa và giá trị tương ứng của nó.
    for key, value in hearders.items():
        print(key,":",value)

if __name__ == '__main__':
    chrome_user_agent()


