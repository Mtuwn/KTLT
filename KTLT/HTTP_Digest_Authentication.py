import requests
# HTTPDigestAyth là một lớp được cung cấp trong thư viện request.auth của Python để xác thực qua phương thức băm thông tin đăng nhập(digest authentication)
# Phương thức này được sử dụg để tăng cường bảo mật so với phương thức xác thực cơ bản
from requests.auth import HTTPDigestAuth
# getpass là một hàm được sử dụng để nhập mật khẩu từ người dùng mà không hiển thị mật khẩu người dùng
from getpass import getpass

user=input("Enter user:")
password = getpass()
url='http://httpbin.org/digest-auth/auth/user/pass'
# Chúng ta gửi 1 request get tới url đã xây dựng và sử dụng phương thức xác thực là Digest với tên người dùng và mật khẩu được cung cấp
response = requests.get(url,auth=HTTPDigestAuth(user,password))
print("Header request:")
# Vòng for này duyêht qua tất cả các phần tử của request header và in ra các header và value tương ứng
for header,value in response.request.headers.items():
    print(header,":",value)
# Dòng này xuất stutus của response
print("\nResponse.status_code:",str(response.status_code))
if (response.status_code == 200):
    print("Login successful:", str(response.json()))

# Lặp qua các header của response và in ra tên các header và value tương ứng
for header,value in response.headers.items():
    print(header,":",value)