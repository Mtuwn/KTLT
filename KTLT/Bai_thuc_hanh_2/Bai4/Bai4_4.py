# Modun os là một thư viện tiêu chuẩn cung cấp các chức năng để tương tác với hệ điều hành
# Các chức năng của nó như: Quản lý đường dẫn và thư mục, tương tác với biến môi trường, thực thi lệnh hệ thống, tạo, đổi tên và xóa tệp tin,thông tin về hệ thống
import os

# Thêm đường dẫn đến thư mục chứa Nmap vào biến môi trường PATH tạm thời
# os.pathsep là một hằng số định nghĩa ký tự phân cách đường dẫn trong biến môi trường PATH (trong Windows, đây thường là dấu chấm phẩy ;).
# r"C:/Program Files (x86)/Nmap" là đường dẫn đến thư mục chứa Nmap
# os.environ["PATH"] truy cập vào biến môi trường PATH và += được sử dụng để thêm đường dẫn mới vào cuối danh sách
os.environ["PATH"] += os.pathsep + r"C:/Program Files (x86)/Nmap"

# Thực thi lệnh Nmap
os.system("nmap -sT 127.0.0.1")
