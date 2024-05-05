def min(a,b):
    return a if a<b else b

def last_occurrence(P,x):
    for i in range(len(P)-1,-1,-1):
        if P[i] == x:
            return i
    
    return -1

def boyer_moore_search(T,P):
    m = len(P)
    i = m-1
    j = m-1
    flag = False

    while i < len(T):
        if(T[i] != P[j]):
            i = i + m - min(j, 1 + last_occurrence(P, T[i]))
            j = m - 1
        else: 
            if j == 0:
                print("\nVi tri xuat hien cua P trong T la", i)
                flag = True
                return
            i -= 1
            j -= 1
    
    if not flag:
        print("\nNot found!")
        return

T = input("Nhap chuoi T: ")
P = input("Nhap chuoi P: ")
    

boyer_moore_search(T, P)