import random
import math

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

def isPrime(n):
    return n==2 or (n > 2 and all(n % i != 0 for i in range(2, int(math.sqrt(n))+1)))

def nhanBinhPhuongCoLap(a,k,n):
    b = 1
    if k == 0:
        return b
    A = a
    if k%2 == 1:
        b = A
    k //= 2
    while k != 0:
        A = A * A % n
        if k % 2 == 1:
            b = A * b % n
        k //= 2
    return b

def mod_inverse(a, b):
    x,y,z = 0,1,b
    
    while b > 0:
        q = a//b
        a,b = b, a%b
        x,y = y -x*q, x
    
    return y+z if y<0 else y

sbd = int(input("Nhap SBD: "))
while True:
    q, p = random.sample([i for i in range(101,500) if isPrime(i)],2)
    n, phi = p*q, (p-1)*(q-1)
    e = random.choice([i for i in range(2,phi) if gcd(i,phi) == 1])
    d = mod_inverse(e,phi)
    m = sbd+123
    if ( n > m):
        break
c = nhanBinhPhuongCoLap(m,e,n)
print("Encrypt: c =", c)
print("Decrypt: m =", nhanBinhPhuongCoLap(c, d, n)-123)

