import math

max = 100

def isQprime(n):
    cnt = 0
    for i in range(1,n+1):
        if(n%i == 0):
            cnt = cnt + 1
    if(cnt == 4):
        return True
    else: return False

def main():
    n = int(input("Nhập n: "))
    flag = False
    for i in range(1, n+1):   
        if isQprime(i) is True:
            flag = True
            print(i, end=" ")
    
    if flag is False:
        print("No")

if __name__=="__main__":
    main()