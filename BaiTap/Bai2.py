import math

def eratosthenes(a,b):
    primes = [1]*(b-a+1)

    for i in range(2, int(math.sqrt(b)+1)):
        for j in range(max(i*i, (i+a-1)//i*i), b+1,i):
            primes[j-a] = 0
    for i in range(a, b + 1):
        if primes[i - a]:
            print(i, end=" ")        
def main():
    n = int(input("Nhap N: "))
    a = 10**(n-1)
    b = 10**n -1 
    eratosthenes(a,b)

if __name__ =="__main__":
    main()