import random

def nhanBinhPhuongCoLap(a,k,n):
    b = 1
    if  k == 0: 
        return b
    A = a
    if k % 2 == 1:
        b = A
    
    while k != 0:
        A = pow(A,2,n)
        if(k%2 == 1):
            b = A*b%n
        k //=2
    
    return b

def fermat(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    
    k = 10

    for i in range(1,k):
        a = random.randint(2,n-2)
        r = nhanBinhPhuongCoLap(a,n-1,n)
        
        if r != 1:
            return False
    
    return True

n = int(input('Nhap vao so tu nhien n: '))
if fermat(n):
    print(f"{n} la nguyen to")
else: print(f"{n} khong la nguyen to")