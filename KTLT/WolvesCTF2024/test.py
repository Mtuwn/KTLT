import jwt
from datetime import datetime, timedelta

# Đọc private key từ file
with open('private.pem', 'r') as f:
    private_key = f.read()

# Đọc public key từ file
with open('public.pem', 'r') as f:
    public_key = f.read()

# Payload của JWT
payload = {
    'sub': 'user123',
    'name': 'John Doe',
    'iat': datetime.utcnow(),  # Thời gian phát hành JWT
    'exp': datetime.utcnow() + timedelta(hours=1)  # Thời gian hết hạn của JWT (1 giờ sau khi phát hành)
}

# Tạo JWT
token = jwt.encode(payload, private_key, algorithm='ES256')

print('Token:', token)

# Xác thực JWT
try:
    decoded = jwt.decode(token, public_key, algorithms=['ES256'])
    print('Thông tin giải mã:', decoded)
except jwt.ExpiredSignatureError:
    print('JWT hết hạn')
except jwt.InvalidTokenError:
    print('JWT không hợp lệ')
