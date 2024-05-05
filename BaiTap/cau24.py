import math

def isPrime(n):
    if n <= 1: return False
    if n == 2: return True
    else:
        for i in range(2, math.ceil(math.sqrt(n) +1)):
            if n % i == 0:
                return False
    return True

def count(a,b,s1,s2):
    S = []
    for i in s1:
        for j in s2:
            sum = i+j
            if sum >= a and sum <= b and isPrime(sum):
                if sum  not in S:
                    S.append(sum)
    return S

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
S1 = [i*i for i in range(1, int(math.sqrt(b))+1)]
S2 = [i*i for i in range(1, int(math.sqrt(b))+1)]

result = count(a,b,S1,S2)
if len(result) > 0:
    print(result)
    print(f'Số lượng : {len(result)}')
else:
    print('Không có giá trị nào')