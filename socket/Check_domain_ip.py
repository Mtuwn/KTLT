import socket

def resolve_domain(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

if __name__ == "__main__":
    domain_name = input("Nhập tên miền: ")
    ip_address = resolve_domain(domain_name)
    if ip_address:
        print(f"Địa chỉ IP của {domain_name} là: {ip_address}")
    else:
        print(f"Không thể tìm thấy địa chỉ IP cho {domain_name}")
