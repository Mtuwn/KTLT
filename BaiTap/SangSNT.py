import math

check = [0]*100000

def SangEratosthenes(n):
    for i in range(2,n+1):
        check[i] = 1
    
    i = 2
    while i<=n:
        if check[i] == 1:
            print(i, end=" ")
            for j in range(2*i, n+1, i):
                check[j] = 0
        i += 1

n = int(input("Nhap N: "))
SangEratosthenes(n)
        