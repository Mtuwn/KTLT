# Modun Shodan cho phép tương tác với api shodan để tìm kiếm cac thiết bị và máy chủ trên internet
import shodan

# Khởi tạo danh sách servers để lưu trữ địa chỉ ip của các máy chủ được tìm thấy
servers = []
# shodan_api_key lưu trữ giá trị api được lấy từ https://account.shodan.io/
shodan_api_key = 'PJEwcscZgElwX5oNsCG3Xu0pPrYSpI7x'
# Tạo một đối tượng shodan mới bằng cách gọi hàm khởi tạo của lớp shodan và truyền khóa api để khởi tạo
# Đối tượng (shodan) này sẽ được sử dụng để thực hiện tìm kiếm
SHODAN = shodan.Shodan(shodan_api_key)

try:
    # Sử dụng phương thức search của đối tượng SHODAN để tìm kiếm các thiết bị có cổng mở 21(thường dùng cho FTP) của người dùng ẩn danh đã đăng nhậo
    # Kết quả trả về được lưu trữ ở biến results
    results = SHODAN.search("port:21 Anonymous user logged in")
    # In ra số lượng máy chủ được tìm thấy bằng cách đếm số phần tử trong danh sách kết quả
    # results['matches'] là danh sách các kết quả tìm kiếm, mỗi phần tử đại diện cho một kết quả
    # matches là một trường dữ liệu trong kết quả trả về từ việc sử dụng api shodan
    #  Trường này chứa danh sách các kết quả tìm kiếm, mỗi kết quả là một đối tượng json mô tả một thiết bị hoặc máy chủ mà shodan tìm được
    print("Số lượng máy chủ: ", str(len(results['matches'])))
    # Duyệt qua từng kết quả trong danh sách kết quả
    for result in results['matches']:
        # Nếu địa chỉ của danh sách đó không phải là none thì được thêm vào danh sách servers bằng hàm append()
        if result['ip_str'] is not None:
            servers.append(result['ip_str'])
    # Duyệt qua từng phần tử trong danh sách servers và xuất ra màn hình
    for server in servers:
        print(server)
except shodan.APIError as e: # Bắt các ngoại lệ do api shodan gây ra. Nếu xảy ra lỗi, nó sẽ in thông báo lỗi
    print('Error: {}'.format(e))
