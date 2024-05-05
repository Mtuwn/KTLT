# # Modun urllib.request là một modun của Python cung cấp chức năng mở url, đọc và gửi dữ liệu
# # Nó thường được sử dụng để truy cập các trang web hoặc tương tác với máy chủ web từ bên trong chương trình python

import urllib.request

# biến url để lưu địa chỉ url 
url='http://python.org'
# Biến user_agent dùng để lưu loại thiết bị, hệ điều hành và trình duyệt đang được yêu cầu đến máy chủ
USER_AGENT = 'Mozilla/5.0 (Linux; Adroid 10) AppleWebKit/537.36'

def chrome_user_agent():
    # urllib.request.build_opener() là phương thức dùng để tạo một opener
    # Opener là đối tượng sử dụng để mở và xử lý yêu cầu HTTP hoặc Url khác trong python
    opener = urllib.request.build_opener()
    # opener.addheaders dùng để thiết lập hoặc thay đổi header của một opener
    # Trong HTTP, header User-Agent được sử dụng để xác định loại trình duyệt hoặc ứng dụng web nào đang gửi yêu cầu
    opener.addheaders = [('User-agent',USER_AGENT)]
    # urllib.request.install_opener(opener) là hàm để sử dụng để cài đặt một opener cho toàn bộ ứng dụng
    # Khi một opener được cài đặt bằng cách này, mọi yêu cầu HTTP được tạo ra sau đó trong mọi ứng dụng sẽ sử dụng opener này để gửi yêu cầu thay vì opener mặc định
    urllib.request.install_opener(opener)
    # urllib.request.urlopen() dùng để mở url và nội dung trả về sẽ được lưu trữ vào biến response
    # Nội dung phản hồi chứa thông tin về phản hồi từ server khi gửi request yêu cầu HTTP đến Url cụ thể
    response = urllib.request.urlopen(url)
    print("Respone header")
    print("------------------------")
    # Vòng for được sử dụng để in ra các header và giá trị tương ứng của phản hồi HTTP
    for header,value in response.getheaders():
        print(header,":", value)


if __name__ == '__main__':
    chrome_user_agent()
