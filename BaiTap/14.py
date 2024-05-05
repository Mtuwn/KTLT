import math
def sangNT():
    a, b = 100, 999

    primes = [1] * (999-100+1)
    for i in range(2, int(math.sqrt(b)+1)):
        for j in range(max(i*i, (i+a-1)//i*i),b+1, i):
            primes[j-a] = 0
    
    lists = []
    for i in range(a, b+1):
        if primes[i-a] == 1:
            lists.append(i)

    return lists

def reverse_num(n):
    reverse = 0
    while n > 0:
        last = n % 10
        reverse = reverse*10 + last
        n //= 10
    return reverse

def solve():
    lists = []
    primes = sangNT()
    for i in range(len(primes)):
        reserve = reverse_num(primes[i])
        tam = 2
        while tam < reserve:
            if pow(tam,3) == reserve:
                lists.append(primes[i])
            
            tam += 1
    
    print(lists)

solve()