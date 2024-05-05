import math
import random

def check(n):
    if n == 2 or n == 3:
        return True
    if n < 2 :
        return False

    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    
    return True

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

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

def solve(n):
    if check(n):
        return False
    
    b = 2
    while(b < n):
        if gcd(b,n) == 1:
            u = nhanBinhPhuongCoLap(b, n-1,n)
            if u != 1:
                return False
        
        b += 1

    return True

    

n = int(input("Nhap N: "))
for i in range(2, n+1):
    if solve(i):
        print(i)
