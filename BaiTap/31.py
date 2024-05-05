import math

def isPrime(x):
    if x <= 1: return False
    if x == 2: return True
    else:
        for i in range(2, math.ceil(math.sqrt(x) +1)):
            if x % i == 0:
                return False
    return True

def nearest_prime(n):
    lower = n -1 
    upper = n + 1

    while True:
        if isPrime(lower):
            return lower
        elif isPrime(upper):
            return upper
        
        lower -= 1
        upper += 1

sbd = int(input("Nhap SBD: "))
k = nearest_prime(sbd)
result = pow(sbd,k,123456)
print(result)
