import math

def find_reverse(n):
    reverse_num = 0
    while n > 0:
        last_num = n % 10
        reverse_num = reverse_num*10 + last_num
        n //= 10
    
    return reverse_num

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

def check(x):
    if x <= 1: return False
    if x == 2: return True
    else:
        for i in range(2, math.ceil(math.sqrt(x) +1)):
            if x % i == 0:
                return False
    return True

def find_emirp(n):
    primes = find_primes(n)
    lists = []
    for i in range(len(primes)):
        reverse_num = find_reverse(primes[i])
        if check(reverse_num):
            lists.append(primes[i])
    
    print(lists)

find_emirp(int(input("Nhap n: ")))