import math
def sangNt(a,b):
    primes = [1]*(b-a+1)

    for i in range(2, int(math.sqrt(b)+1)):
        for j in range(max(i*i,(i+a-1)//i*i),b+1, i):
            primes[j-a] = 0
    sum = 0
    for i in range(a,b+1):
        if primes[i-a] == 1:
            sum += i
    
    print(sum)

a = int(input("Nhap A: "))
b = int(input("Nhap B: "))
sangNt(a,b)