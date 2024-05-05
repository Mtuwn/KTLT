import math

def check(x):
    if x <= 1: return False
    if x == 2: return True
    else:
        for i in range(2, math.ceil(math.sqrt(x) +1)):
            if x % i == 0:
                return False
    return True

def find_primes(n):
    primes = [1]*(n+1)
    lists = []
    for i in range(2,n+1):
        if primes[i] == 1:
            for j in range(i*i, n+1, i):
                primes[j] = 0
    
    for i in range(2,n+1):
        if primes[i] == 1:
            lists.append(i)
    return lists

def solve(a,b):
    primes_all = find_primes(b) # số nguyên tố từ 2 tới b
    primes_AB = [] # số nguyên tố trong khoảng AB
    lists = [] # Lưu chữ kêt quả cần tìm
    for i in primes_all:
        if i >= a and i <= b:
            primes_AB.append(i)
    
    for i in primes_AB:
        sum = 0
        for j in primes_all:
            if(j == i):
                if check(sum):
                    lists.append(i)
                break
            sum += j
    print(lists)
        


a = int(input("Nhap A: "))
b = int(input("Nhap B: "))
solve(a,b)