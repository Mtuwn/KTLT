
def euclide(a,b):
    x,y,z = 0,1,b
    print(a,b)
    while b > 0:
        q = a//b
        a,b = b, a%b
        x,y = y -x*q, x
    
    return a

m = int(input("Nhap M: "))
n = int(input("Nhap N: "))
d = int(input("Nhap D: "))
lists = []
for i in range(m, n+1):
    for j in range(i+1, n+1):
        if euclide(j,i) == d:
            lists.append((i,j))

print(lists)