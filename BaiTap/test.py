import pyautogui
import subprocess
import time

# Địa chỉ IP hoặc tên máy chủ của máy tính Windows 10 từ xa
remote_host = "192.168.255.132"

# Tên người dùng và mật khẩu để đăng nhập vào máy tính từ xa
username = "trantuan"
password = "16040312b"

# Khởi động kết nối RDP
subprocess.run(["mstsc", "/v:" + remote_host])


# Đợi một chút để cửa sổ kết nối RDP hiện ra trantuan    16040312b

time.sleep(5)

# Sử dụng pyautogui để nhập tên người dùng và mật khẩu
pyautogui.write(username)
pyautogui.press('tab')
pyautogui.write(password)
pyautogui.press('enter')
