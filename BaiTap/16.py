import random
import math

def check(x):
    if x <= 1: return False
    if x == 2: return True
    else:
        for i in range(2, math.ceil(math.sqrt(x) +1)):
            if x % i == 0:
                return False
    return True

def main():
    N = int(input("Nhập kích thước của mảng (N): "))
    list_radom = [random.randint(1, 1000) for i in range(N)]
    for i in list_radom:
        if check(i):
            print(i, end=" ")

if __name__ == "__main__":
    main()