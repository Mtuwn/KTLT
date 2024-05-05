import math
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

def solve(n):
    primes = find_primes(n)

    for i in range(len(primes)-3):

        if primes[i]+primes[i+1]+primes[i+2]+primes[i+3] <= n and check(primes[i]+primes[i+1]+primes[i+2]+primes[i+3]):
            print(primes[i],primes[i+1],primes[i+2],primes[i+3])

solve(int(input("Nhap N: ")))