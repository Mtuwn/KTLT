# Một thư viện phổ biến dùng để giúp lập trình viên có thể thực hiện cac tác vụ như gửi request tới server
# Cũng như xử lý response một cách đơn giản
import requests

# Biến url chứa địa chỉ url mà ta muốm gửi yêu cầu đến
url='http://python.org'

def chrome_user_agent():
    # Dòng này gửi 1 request get tới url chỉ định
    # Kết quả trả về được lưu trong biến r 
    r = requests.get(url)

    # Vòng lặp for lặp qua tất cả các phần từ trong dictionary r.headers chứa các header được trả về của server
    # Hàm items() được sử dụng để trả về một danh sách các cặp (hoặc tuple) khóa-giá trị từ một từ điển (dictionary). Mỗi cặp này bao gồm một khóa và giá trị tương ứng của nó.
    for key,value in r.headers.items():
        # Xuất dữ liệu
        print(key,":",value)

if __name__ == '__main__':
    chrome_user_agent()
