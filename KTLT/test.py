# Một thư viện phổ biến dùng để giúp lập trình viên có thể thực hiện cac tác vụ như gửi request tới server
# Cũng như xử lý response một cách đơn giản
import requests

# Biến url chứa địa chỉ url mà ta muốm gửi yêu cầu đến
url='https://gauntlet-okntin33tq-ul.a.run.app/hidden83365193635473293'


def chrome_user_agent(pos,cookie):
    # Dòng này gửi 1 request get tới url chỉ định
    # Kết quả trả về được lưu trong biến r 
    Cook = {'jwt-uncrackable-cookie-counter': f'{cookie}'}
    r = requests.get(url, cookies=Cook)
    print("Lần 1: ",pos)
    cookies_dict = r.cookies.get_dict()
    jwt_cookie_value = cookies_dict.get('jwt-uncrackable-cookie-counter', '')
    if(pos == 1001):
        print(r.text)
    return jwt_cookie_value
 

if __name__ == '__main__':
    pos = 0
    cookie = ""
    for i in range(1,1005):
        cookie = chrome_user_agent(pos,cookie)
        print("cookie:",cookie)
        pos = pos + 1