def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(n, m, primes, len, res, pos):
    if n == 0 and m == 0:
        for i in range(pos - 1, -1, -1):
            if i != 0:
                print(res[i], end=",")
            else:
                print(res[i], end="")
        print()
        return
    if n <= 0 or m <= 0:
        return

    for i in range(len):
        if n >= primes[i]:
            res[pos] = primes[i]
            find_primes(n - primes[i], m - 1, primes, i, res, pos + 1)

if __name__ == "__main__":
    n = int(input("Nhap so nguyen duong n: "))
    m = int(input("Nhap so nguyen to m: "))
    
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    res = [0] * m
    find_primes(n, m, primes, len(primes), res, 0)
