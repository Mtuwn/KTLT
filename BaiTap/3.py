import math
def isPrimes(x):
    if x == 2 or x == 3:
        return True
    if x < 2 or x % 2 == 0:
        return False
    
    for i in range(2, math.ceil(math.sqrt(x))):
        if x % i == 0:
            return False
    
    return True
def calculate(n):
    lists = []
    for i in range(1,n+1):
        if n%i == 0:
            lists.append(i)

    list_primes = []
    q,p,k,s = 0,0,0,0

    for i in range(len(lists)):
        p += lists[i]
        s += 1
        if isPrimes(lists[i]):
            k += 1
            q += lists[i]
    return n + p + s - q - k

def main():
    n = int(input("Nhap N: "))
    print(calculate(n))

if __name__ == "__main__":
    main()