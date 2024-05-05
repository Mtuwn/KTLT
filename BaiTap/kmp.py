
def failure_function(P):
    j = 2 # Biến chạy số thứ tự trong bảng F
    i = 0 # Biến chạy vị trí trong chuỗi P
    F = [-1]+[0]*(len(P) -1) # Khởi tạo bẳng F với các giá trị mặc định tại vị trí 0 và 1 là -1 và 0
    #Kiểm tra tiền tố và hậu tố trùng nhau
    while j < len(P):
        if P[j-1] == P[i]:
            F[j] = i+1
            i += 1
            j += 1
        elif i > 0:
            i = F[i]
        else: 
            F[j] = 0
            j += 1
    return F

def KMP(T, P, F):
    i = 0 # Vị trí biến chạy trong T
    j = 0 # Vị trí biến chạy trong P

    while i+j < len(T):
        
        if P[j] == T[j+i]:
            j += 1
            if j == len(P):
                return i
        else: 
            if F[j] > -1:
                i += j - F[j]
                j = F[j]
            else:
                j = 0
                i += 1
    
    return -1

def main():
    T = input("Nhap chuoi T: ")
    P = input("Nhap chuoi P: ")
    F = failure_function(P)

    result = KMP(T, P, F)
    if result != -1:
        print("Vi tri xuat hien P trong T la:", result)
    else:
        print("Khong tim thay!!!")

if __name__ == "__main__":
    main()